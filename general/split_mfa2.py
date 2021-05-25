from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description="Split the fasta file into individual file with each gene seq")
parser.add_argument('-f', action='store', dest='fasta_file', help='Input fasta file')
result = parser.parse_args()

f_open = open(result.fasta_file, "r")
name = result.fasta_file.replace(".nextpolish.fasta", "")

used_names = []

for rec in SeqIO.parse(f_open, "fasta"):
    filename = name + "_" + rec.id + ".fasta"
    seq = rec.seq
    if filename not in used_names:
        used_names.append(filename)
        id_file = open(filename, "w")
        id_file.write(">"+str(filename)+"\n"+str(seq))
        id_file.close()
    else:
        filename = name + "_" + rec.id + "_1.fasta"
        used_names.append(filename)
        id_file = open(filename, "w")
        id_file.write(">"+str(filename)+"\n"+str(seq))
        id_file.close()

f_open.close()
