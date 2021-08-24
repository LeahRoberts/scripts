#!/usr/bin/python
from Bio import SeqIO
import sys
cmdargs = str(sys.argv)
for seq_record in SeqIO.parse(str(sys.argv[1]), "fasta"):
	name = seq_record.id
	output_line = '%s\t%i' % \
	(name, len(seq_record))
	print(output_line)
