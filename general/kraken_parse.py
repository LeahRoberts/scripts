#!/user/bin/env python

# write script to count and parse out lines with 2nd species percentage higher than x threshold

import sys

# Read in file:

file1 = sys.argv[1]
cutoff = sys.argv[2]

w = open(file1, "r")

with open("contaminated.list", "a") as fout:
    for line in w.readlines():
        species2 = line.split("\t")[16].rstrip("%")
        if float(species2) > int(cutoff): 
            fout.write(line)

