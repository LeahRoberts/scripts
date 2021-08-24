#!/usr/bin/env python

# count the total base pairs in a bed file:

import sys

bed_file = sys.argv[1]

count = 0

with open(bed_file, "r") as fin:
	for line in fin:
		start = line.split("\t")[1].rstrip()
		end = line.split("\t")[2].rstrip()
		diff = int(end) - int(start)
		count = count + diff

print("Total = ", count)
