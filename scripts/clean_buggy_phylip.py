# Converts sequence alignments to format compatible with bppml

from Bio import AlignIO
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", help="alignment file to clean")
parser.add_argument("--output_file", help="output file name")
parser.add_argument("--outdir", help="base directory for output")
args = parser.parse_args()
print(args)

basedir = args.outdir
infile = args.input_file
outfile = args.output_file

if not os.path.exists(basedir):
    os.makedirs(basedir)

input_handle = open(infile, "rU")
output_handle = open("{}/{}".format(basedir, outfile), "w")

alignments = AlignIO.parse(input_handle, "phylip-relaxed")
AlignIO.write(alignments, output_handle, "fasta")

output_handle.close()
input_handle.close()

