#!/user/bin/env python

# Assign isolate to one of two lists:

import sys

BM_list = []
NH_list = []

# read in file with seqID and "isolate" name, looks like this:
# mv <seqID>.fasta <isolate>.fasta

file1 = sys.argv[1] # file with sequencing name and isolate name

w = open(file1, "r")

for line in w.readlines():
    seq_name = line.split(" ")[1].rstrip(".fasta") #seq name
    iso_name = line.split(" ")[2].rstrip(".fasta\n") #isolate name
    if iso_name.startswith('B'):
        BM_list.append(seq_name)
    elif iso_name.startswith('N'):
        NH_list.append(seq_name)

with open('BM_list.txt', 'a') as bout:
    for n in BM_list:
        bout.write("%s\n" % (n))

with open('NHTD_list.txt', 'a') as nout:
    for x in NH_list:
        nout.write("%s\n" % (x))
