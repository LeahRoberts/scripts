#!/usr/bin/env python

# Script for transposing all of the clusters and numbering them
# Need to remove the first line header and commas at the end of each line
# after getting the cluster csv from Transcluster

# This is just to make it easier to dereplicate based on patient 

import sys

line_number = 1

fout = open("transposed_clusters.csv", "a")

with open(sys.argv[1], "r") as fin:
    for line in fin.readlines():
        iso_count = len(line.split(","))
        for i in range(int(iso_count)):
            name = line.split(",")[i].rstrip()
            cluster = str(line_number)
            fout.write("%s,%s\n" % (name, cluster))
        line_number += 1
