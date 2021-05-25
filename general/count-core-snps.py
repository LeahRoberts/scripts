#!/usr/bin/env python

import sys
import os

def define_file(input):
    '''
    Edit the output file name
    '''
    name = os.path.splitext(input)[0]
    return(name)

file = sys.argv[1]
f = open(file, "r")
lines = f.readlines()

count = 0

for line in lines:
    REF = line.split("\t")[2].rstrip
    FIRST = line.split("\t")[3].rstrip
    LAST = line.split("\t")[4].rstrip
    if REF == FIRST:
        if FIRST != LAST:
            count += 1

with open("summary_snps.txt", "a") as p:
    file = define_file(sys.argv[1])
    p.write("%s\t%s\n" % (file, count))
