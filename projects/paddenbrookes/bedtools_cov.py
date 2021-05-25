#!/usr/bin/env python


#To do:

# 1. take bam file and run bedtools
# 2. get each contig + cov into separate files/lists? 
# 3. calculate average coverage
# 4. figure out which is the longest contig (make this the chr)
# 5. divide all plasmids by the chromosome (to get proportional coverage)


import sys
import subprocess
from subprocess import CalledProcessError
import pandas as pd
import operator

def bashcommand(command):
	'''
	Execute a shell command by concatenating a string
	and executing using subprocesses
	'''
# 	with open("command_log.txt", "a") as fout:
# 		fout.write("%s\n" % command)
	try:
		subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except CalledProcessError as e:
		print(e.output)


bam_file = sys.argv[1]
bed_file = bam_file.split(".")[0] + ".cov.bed"
outfile = bam_file.split(".")[0] + ".cov.out"

bashcommand("bedtools genomecov -d -ibam %s > %s" % (bam_file, bed_file)) # run bedtools
print("Finished bedtools")

df = pd.read_csv(bed_file, sep='\t', names=['contig', 'position', 'coverage'])
contigs = df['contig'].unique()

lengths = {}
covs = {}

print("starting coverage calculations")
with open (outfile, "a") as fout:
	fout.write("contig\tlength\tavg_cov\n") 
	for i in contigs: 
		new_df = df[df["contig"].isin([i])]
		contig_length = len(new_df.index)
		all_cov = new_df['coverage'].sum()
		lengths[i] = contig_length
		average = int(all_cov)/int(contig_length)
		covs[i] = average
		fout.write("%s\t%s\t%s\n" % (i, contig_length, average))
		
chr = max(lengths.items(), key=operator.itemgetter(1))[0]
print("setting chromosome to", chr)

with open(outfile, "a") as fout:
	fout.write("plasmid\tchr\tprop_cov\n")
	for key in covs.keys():
		if key != chr:
			cov = covs[key]
			denom = covs[chr]
			prop = int(cov)/int(denom)
			fout.write("%s\t%s\t%s\n" % (key, chr, prop))