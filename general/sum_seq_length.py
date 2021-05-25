#!/usr/bin/python
#parses sequence lengths from a file and prints them to the screen
#usage python seqlength.py infasta
from __future__ import print_function
from sys import argv
import sys
try:
    from Bio import SeqIO
except:
    print("script requires BioPython to run..exiting")
    sys.exit()
try:
    handle = open(argv[1], newline=None)
except:
    print("usage: script input.fasta")
    sys.exit()

totals = []

for record in SeqIO.parse(handle, "fasta"):
    totals.append(len(record.seq))

print(sum(int(x) for x in totals))

handle.close()
