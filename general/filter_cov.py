#!/usr/bin/env python

import sys
import re

try:
	from Bio import SeqIO
except:
	print("script requires BioPython to run..exiting")
	sys.exit()
try:
	handle = sys.argv[1]
	cov = sys.argv[2]
except:
	print("usage: script input.fasta cov_cutoff")
	sys.exit()

name = handle.rsplit(".", 1)[0]

outfile = re.sub(r"\.\w+$", r".modified.fa", handle)

with open(outfile, "a") as fout:
	for record in SeqIO.parse(handle, "fasta"):
		header = record.id
		coverage = header.split("_")[5]
		coverage = float(coverage.rstrip())
		if coverage >= int(cov):
			fout.write(">%s\n" % (record.id))
			fout.write("%s\n" % (record.seq))
