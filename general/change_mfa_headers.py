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
except:
	print("usage: script input.fasta")
	sys.exit()

name = handle.rsplit(".", 1)[0]

outfile = re.sub(r"\.\w+$", r".modified.fa", handle)

with open(outfile, "a") as fout:
		counter = 1
		for record in SeqIO.parse(handle, "fasta"):
			seq = record.seq
			header = name + "_" +  str(counter)
			fout.write(">%s\n" % (header))
			fout.write("%s\n" % (str(seq)))
			counter += 1
