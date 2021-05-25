#!/usr/bin/python

from Bio import SeqIO
import sys

mfa = sys.argv[1]
name = mfa.replace(".fasta", "")


fasta_sequences = SeqIO.parse(open(mfa),'fasta')
count = 0
for fasta in fasta_sequences:
	count += 1 
	outfile = name + "." + str(count) + ".fasta" 
	with open(outfile, 'w') as fout:
		SeqIO.write(fasta, fout, 'fasta')
