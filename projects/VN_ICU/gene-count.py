#!/user/bin/env python

import sys
import csv

file1 = sys.argv[1] 

num = {}

fin = open(file1, "r")
for line in fin.readlines():
	gene = line.rstrip()
	if gene not in num:
		num[gene] = 1
	else:
		num[gene] += 1

w = csv.writer(open("gene-counts.csv", "w"))
for key, val in num.items():
	w.writerow([key, val])
