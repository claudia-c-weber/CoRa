import os.path
import glob
import re
import matplotlib.pyplot as plt
import pandas as pd

def parse_mm_out(indir, outfile):
    results = glob.glob(indir + "*.output")
    of = open(outfile, "w")
    print("Writing to {}".format(outfile))
    of.write("file\titer\tL_M0\tL_CoRa\tLR\tOmega_M0\tOmega_Co\tOmega_Ra\tlength\tsig_LR\tCo_greater\ttreelength_M0\ttreelength_CoRa\n")
    for r in results:
        output = open(r, "r").read()
        i = r.split(".")[1].split("/")[-1]
        if "Error" in output:
            print("Couldn't read!!")
        else:
            output = output.split("Making random Radical matrix -> <Random.mat>")
            try:
                L_M0 = re.search("Final lnL: ([\-0-9.]+)", output[0]).group(1)
                L_CoRa = re.search("Likelihood:\t([\-0-9.]+);", output[1]).group(1)
                Omega_M0 = re.search("Parameter\[13\]\tOmega = ([0-9.]+);", output[0]).group(1)
                Omega_Co = re.search("Omega_Conservative = ([0-9.]+);", output[1]).group(1)
                Omega_Ra = re.search("Omega_Radical = ([0-9.]+);", output[1]).group(1)
                length = re.search("removal .+ of length ([0-9]+)", output[0]).group(1)
                treelen_M0 = re.search("TreeLength:\t([0-9.]+)\n", output[0]).group(1)
                treelen_CoRa = re.search("TreeLength:\t([0-9.]+)\n", output[1]).group(1)
                LR = 2 * (abs(float(L_M0)) - abs(float(L_CoRa)))
                of.write("\t".join([str(t) for t in [r, i, L_M0, L_CoRa, LR, Omega_M0, Omega_Co, Omega_Ra, length, int(LR > 3.841), int(Omega_Co > Omega_Ra), treelen_M0, treelen_CoRa]]) + "\n")
            except AttributeError:
                of.write("{}\t{}\t{}\n".format(r, i, "\t".join(["NA"]*11)))
                print ("NA")
    of.close()
    return

def parse_bppml_out(indir, outfile):
    results = glob.glob(indir + "*.CoRa.params.txt")
    of = open(outfile, "w")
    print("Writing to {}".format(outfile))
    of.write("file\titer\tL_M0\tL_CoRa\tLR\tOmega_M0\tOmega_Co\tOmega_Ra\tlength\tsig_LR\tCo_greater\n")
    for r in results:
        output_CoRa = open(r, "r").read()
        output_M0 = open(r.replace("CoRa", "M0"), "r").read()
        i = r.split(".")[1].split("/")[-1]
        try:
            L_M0 = re.search("# Log likelihood = ([\-0-9.]+)\n", output_M0).group(1)
            L_CoRa = re.search("# Log likelihood = ([\-0-9.]+)\n", output_CoRa).group(1)
            Omega_M0 = re.search(",omega=([0-9.]+)\)\n", output_M0).group(1)
            Omega_Co = re.search(",omegaC=([0-9.]+)\)\n", output_CoRa).group(1)
            Omega_Ra = re.search(",omegaR=([0-9.]+),", output_CoRa).group(1)
            length = re.search("# Number of sites = ([0-9]+)\n", output_M0).group(1)
            LR = 2 * (abs(float(L_M0)) - abs(float(L_CoRa)))
            of.write("\t".join([str(t) for t in [r, i, L_M0, L_CoRa, LR, Omega_M0, Omega_Co, Omega_Ra, length, int(LR > 3.841), int(Omega_Co > Omega_Ra)]]) + "\n")
        except AttributeError:
            of.write("{}\t{}\t{}\n".format(r, i, "\t".join(["NA"]*9)))
            print ("NA")
    return

parse_mm_out("./output_mm/", "parsed_mm_CoRa.txt")
parse_bppml_out("./output/", "parsed_bppml_CoRa.txt")
