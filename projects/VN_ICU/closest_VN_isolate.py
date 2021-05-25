#!/usr/bin/env python

import sys
import glob

refs = sys.argv[1]

exclude_list = []

def exclude(names):
    with open(names, "r") as fin:
        for line in fin.readlines():
            line = line.rstrip()
            exclude_list.append(line)

exclude(refs)

for file in glob.glob("./*dists"):
    with open("dist_summary.txt", "w") as fout:
        with open(file, "r") as fin:
            for line in fin.readlines():
                iso_1 = line.split("\t")[0]
                iso_2 = line.split("\t")[1]
                if iso_1 not in exclude_list:
                    fout.write(line)
                    break
                elif iso_2 not in exclude_list:
                    fout.write(line)
                    break
