#!/user/bin/env python

# read in two files and get isolate name and species ID in one text file
# move specific species into individual folders

import sys
import csv

file1 = sys.argv[1] # file with sequencing name and isolate name
file2 = sys.argv[2] # file with sequencing name and species ID

# folders to go in to:
# abaum, kpneu, ecoli

species = {}

# put the species ID into a library/dictionary

w = open(file1, "r")
p = open(file2, "r")

for line in p.readlines():
    seqn = line.split("\t")[0].rstrip()
    sp = line.split("\t")[1].rstrip()
    species[seqn] = sp

# Read through file that has sequencing name and isolate name

fout = open("species_with_ID.txt", "a")

for line in w.readlines():
   seq_name = line.split(" ")[1].rstrip(".fasta") #seq name
   iso_name = line.split(" ")[2].rstrip(".fasta\n") #isolate name


   for x, y in species.items():
       if seq_name == x:
           fout.write("%s\t%s\n" % (iso_name, y))

fout.close()

# count the number of species

counts = {}

fin = open("species_with_ID.txt", "r")
for line in fin.readlines():
    isolate = line.split("\t")[0].rstrip()
    species = line.split("\t")[1].rstrip()
    if species not in counts:
        counts[species] = 1
    else:
        counts[species] += 1

w = csv.writer(open("species-counts.csv", "w"))
for key, val in counts.items():
    w.writerow([key, val])
