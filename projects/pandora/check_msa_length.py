#!/usr/bin/env python

# Script for determining:
#
# 1. Number of alleles in MSA
# 2. Min, median and max lengths in MSA

# Requires path to directory containing MSAs
# Requires output filename

from Bio import SeqIO
from Bio.Seq import Seq
import glob
import sys
from statistics import mean, median

file_path = sys.argv[1] + "/*" # path to MSAs
outfile = sys.argv[2] # outfile name, will be tsv file

for file in glob.glob(file_path):
	
	with open(file, "r") as fin:
		count = 0
		for line in fin.readlines():
			if ">" in line:
				count += 1
	
	if count == 0:
		with open(outfile, "a") as fout:
			fout.write("%s\t0\t0\t0\t0\n" % (file))
	else:
		lengths = []
		for record in SeqIO.parse(file, "fasta"):
			record.seq = Seq(str(record.seq).replace("-", ""))
			output_line = len(record.seq)
			lengths.append(output_line)

		max_value = max(lengths, default=0)
		min_value = min(lengths, default=0)
		med_value = median(lengths)

		with open(outfile, "a") as fout:
			fout.write("%s\t%s\t%s\t%s\t%s\n" % (file, count, min_value, med_value, max_value))
