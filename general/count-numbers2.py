#!/user/bin/env python

# read in two files and get isolate name and species ID in one text file
# move specific species into individual folders

import sys
import csv

file1 = sys.argv[1] # file with sequencing name and isolate name

count = {}

fin = open(file1, "r")
for line in fin.readlines():
	item = line.rstrip()
	if item not in count:
		count[item] = 1
	else:
		count[item] += 1

w = csv.writer(open("counts.csv", "w"))
for key, val in count.items():
	w.writerow([key, val])
