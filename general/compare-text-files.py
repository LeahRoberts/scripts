#!/user/bin/env python

import sys
import csv

file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')

list1 = []
list2 = []

for line1 in file1:
    list1.append(line1.rstrip())

for line2 in file2:
    list2.append(line2.rstrip())

dif = set(list1).symmetric_difference(set(list2))

with open("differences_summary.txt", "w") as fout:
    for i in dif:
        print(i)
        fout.write("%s\n" % (i))

