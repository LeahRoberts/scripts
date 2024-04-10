#!/usr/bin/env python

import sys

gff_file = sys.argv[1]

file_name = gff_file.split(".")[0]
outfilename = file_name + ".fasta"

with open(gff_file, "r") as fin:
    with open(outfilename, "a") as fout:
        condition = 0
        for line in fin:
            if line[0] == ">":
                condition = 1
            if condition == 0:
                continue
            else:
                fout.write(line)
