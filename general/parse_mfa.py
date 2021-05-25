#!/usr/bin/python

from Bio import SeqIO
import sys

headers = sys.argv[1]
mfa = sys.argv[2]

list = []

with open(headers, "r") as fin:
    for line in fin.readlines():
        name = line.rstrip()
        list.append(name)


fasta_sequences = SeqIO.parse(open(mfa),'fasta')
with open("parsed_sequences.fasta", 'a') as out_file:
    for fasta in fasta_sequences:
        if fasta.id in list:
            SeqIO.write(fasta, out_file, 'fasta')
