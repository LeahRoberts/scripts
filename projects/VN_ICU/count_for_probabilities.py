#!/user/bin/env python

# count instances of having x SNPs on x days

import sys
import csv

file1 = sys.argv[1]

count = {}

fin = open(file1, "r")
for line in fin.readlines():
	day = line.split("\t")[0].rstrip()
	snp = line.split("\t")[1].rstrip()
	if (day,snp) not in count:
		count[(day,snp)] = 1
	else:
		count[(day,snp)] += 1


w = csv.writer(open("counts.csv", "w"))
for key, val in count.items():
	w.writerow([key, val])
