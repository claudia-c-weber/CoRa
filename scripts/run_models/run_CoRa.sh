# Assumes LSF environment with Anaconda (w. Python 3.6, BioPython),
# Bio++ v. 2.4.0, and ModelOMatic v. 1.04 (development branch) installed.
# Folder must contain Radical.mat

# Notes on defining amino acid partitions in bppml: 
# https://github.com/BioPP/bpp-phyl/blob/master/src/Bpp/Phyl/Model/Codon/AbstractCodonClusterAASubstitutionModel.h
# Amino acids are in alphabetical order (ARNDCQEGHILKMFPSTWYV)
# The default partition (i.e. "partition" parameter not explicitly set) corresponds to the one used in this study.

bpp_basedir=~/workspace/software/bpp/dev/bin/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/workspace/software/bpp/dev/lib64/

#Clean phylip files and convert to fasta to ensure compatibility with bppml
for i in ./phy/*.phy; do
  f=$(basename $i .phy)
  if [ ! -f ./cleaned_fasta/${f}.fst ]; then
    python clean_buggy_phylip.py --input_file ./phy/${f}.phy --output_file ${f}.fst --outdir ./cleaned_fasta;
  fi
done

#Translate
mkdir -p ./cleaned_fasta_AA/
for i in ./cleaned_fasta/*.fst; do f=$(basename $i .fst); ${bpp_basedir}/bppseqman params=SeqMan.bpp DATA=./cleaned_fasta/${f}; done

mv ./cleaned_fasta/*.AA.fst ./cleaned_fasta_AA/

#Generate bionj trees from AA sequence
mkdir -p ./bionj/
for i in ./cleaned_fasta_AA/*.fst; do f=$(basename $i .fst); bsub -o stdout.txt -e stderr.txt -J "bionj" "${bpp_basedir}/bppdist params=Bionj.bpp DATA=${f}"; done

bwait -w "ended(bionj)" #wait for jobs

#Declutter
mv *.AA.mat ./bionj/; mv *.AA.messages ./bionj/; mv *.AA.profile ./bionj/

mkdir -p ./output/

#Run CoRa
for i in ./cleaned_fasta/*.fst; do
  f=$(basename $i .fst);
  if [ ! -f ./output/${f}.CoRa.params.txt ]; then
    bsub -o stdout_CoRa.txt -e stderr_CoRa.txt -J "emp_CoRa" "${bpp_basedir}/bppml params=ML.CoRa.iter.bpp DATA=${f}"
  fi
done

#Run M0
for i in ./cleaned_fasta/*.fst; do
  f=$(basename $i .fst);
  if [ ! -f ./output/${f}.M0.params.txt ]; then
    bsub -o stdout_M0.txt -e stderr_M0.txt -J "emp_M0" "${bpp_basedir}/bppml params=ML.M0.iter.bpp DATA=${f}"
  fi
done

#Run ModelOMatic (not recommended for untested datasets)
#Input must be phylip; uses bionj starting tree
mkdir -p ./output_mm/
for i in ./phy/*.phy; do
  f=$(basename $i .phy)
  if [ ! -f ./output_mm/${f}.output ]; then
    bsub -o stdout_mm.txt -e stderr_mm.txt -J "emp_MM" "~/workspace/software/modelomatic/modelomatic/modelomatic ./phy/${f}.phy > ./output_mm/${f}.output";
  fi
done

#wait for jobs
bwait -w "ended(emp_M0) && ended(emp_CoRa) && ended(emp_MM)" 

#parse output
python parse_CoRa.py
