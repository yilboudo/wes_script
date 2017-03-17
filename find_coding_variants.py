
import sys, os, re
import math

mutation = ("splice_acceptor_variant", "splice_donor_variant", "stop_gained", "frameshift_variant", "stop_lost", "start_lost","protein_altering_variant", "missense_variant", "coding_sequence_variant")

f1 =  open(sys.argv[1], "r")
f2 = open(sys.argv[2], "wa")

array = []
for line in f1:
    line_clean = line.strip()
    if not line_clean.startswith("#"):
        array.append(line)


header = 'SNP REF ALT AF CONSEQUENCE GENE INDIVIDUAL_GENOTYPES'.split(" ")

f2.write("\t".join(header)+"\n")
for line in array:
    if any(s in line for s in mutation):
        f2.write(line)

f2.close()
