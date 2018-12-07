from Bio import AlignIO
import glob
import os
import pandas as pd
#Filter codons for species that use nuclear code 12
#Provided in CTG_clade_list.txt from supplemetary materials
alt_table = pd.read_table("CTG_clade_list.txt")
alternative = [s for s in alt_table.Species]

alignments = glob.glob("./CDS/*fasta")
log = open("logfile_replaced_candida.txt", "w")
error = open("value_error.txt", "w")

outdir = "./phy/"
if not os.path.exists(outdir):
    os.mkdir(outdir)

for al in alignments:
    aid = al.split("/")[-1].split(".")[0]
    try:
        alignment = AlignIO.read(open(al), "fasta")
    except ValueError:
        error.write(aid + "\n")
        continue #something failed
    for i in range(len(alignment)):
        if alignment[i].id in alternative:
            sequence = str(alignment[i].seq)
            codons = [sequence[j:j+3] for j in range(0, len(sequence), 3)]
            if "CTG" in codons:
                indices = [k for k, l in enumerate(codons) if l == 'CTG']
                for ind in indices:
                    codons[ind] = "---"
                    log.write("\t".join([str(e) for e in [aid, alignment[i].id, ind]]) + "\n")
                alignment[i].seq = "".join(codons)
    AlignIO.write(alignment, open(outdir + aid + ".phy", "w"), "phylip-relaxed")

log.close()
error.close()
