#!/user/bin/env python

# read in two files and get isolate name and species ID in one text file
# move specific species into individual folders

import sys
import csv

file1 = sys.argv[1] # file with sequencing name and isolate name

mlst = {}

fin = open(file1, "r")
for line in fin.readlines():
	ST = line.rstrip()
	if int(ST) in range(0, 101):
		if ST not in mlst:
			mlst[ST] = 1
		else:
			mlst[ST] += 1

w = csv.writer(open("mlst-counts.csv", "w"))
for key, val in mlst.items():
	w.writerow([key, val])
