#!/usr/bin/env python

# Script for transposing all of the clusters and numbering them
# Need to remove the first line header and commas at the end of each line
# after getting the cluster csv from Transcluster

# This is just to make it easier to dereplicate based on patient

import sys

fout = open("transposed_genes.csv", "a")

with open(sys.argv[1], "r") as fin:
    for line in fin.readlines():
        iso_count = len(line.split(","))
        for i in range(int(iso_count)):
            name = line.split(",")[i].rstrip()
            gene = line.split(",")[0].rstrip()
            if i == 0:
                pass
            elif i > 0:
                fout.write("%s,%s\n" % (gene, name))
