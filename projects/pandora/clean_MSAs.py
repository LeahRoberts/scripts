#!/user/bin/env python

# Script for cleaning MSAs
# Assumes that the median value is the correct value

# Input:
# path to directory containing MSAs
# value to delete small alleles (<X*median)
# value to delete large alleles (>X*median)

# run as: python clean_MSAs.py <dir/> <lower_limit> <upper_limit>

from Bio import SeqIO
from Bio.Seq import Seq
import glob
import sys
from statistics import mean, median
import os

def output_name(input_file):
    filename = os.path.split(file)[1]
    file_ext = os.path.splitext(file)[1]
    prefix = os.path.splitext(filename)[0]
    final_name = prefix + ".clean" + file_ext
    return final_name

file_path = sys.argv[1] + "/*" # path to MSAs

for file in glob.glob(file_path):

    out_name = output_name(file)
    
    with open(file, "r") as fin:
    	count = 0
    	for line in fin.readlines(): 
    		if ">" in line: 
    		 count += 1
    
    if count == 0:
    	with open("bad_files.txt", "a") as fin:
    		fin.write("%s\n" % (file))
	
	else:

		lengths = []
		# get lengths of all alleles
		for record in SeqIO.parse(file, "fasta"):
			record.seq = Seq(str(record.seq).replace("-", ""))
			output_line = len(record.seq)
			lengths.append(output_line)

		med_value = median(lengths)
		lower_limit = med_value*float(sys.argv[2])
		upper_limit = med_value*float(sys.argv[3])

		# parse only alleles that are within X of the median
		with open(out_name, "a") as fout:
			for record in SeqIO.parse(file, "fasta"):
				aln = Seq(str(record.seq).replace("-", ""))
				if len(aln) < lower_limit:
					pass
				elif len(aln) > upper_limit:
					pass
				else:
					SeqIO.write(record, fout, 'fasta')
