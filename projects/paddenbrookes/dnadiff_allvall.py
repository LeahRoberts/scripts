#!/usr/bin/env python

# all-v-all DNAdiff wrapper

import sys
import glob
import subprocess
from subprocess import CalledProcessError
import pandas as pd
import os

def bashcommand(command):
	'''
	Execute a shell command by concatenating a string
	and executing using subprocesses
	'''

	try:
		subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except CalledProcessError as e:
		print(e.output)

def getlines(file):
	with open(file, "r") as f:
		num_lines = sum(1 for line in f)
	return num_lines

file_path = sys.argv[1] + "/*" # folder containing sequences

names = []
complete = []
complete_2 = []

for file in glob.glob(file_path): # list of all the files
	names.append(file)

test_num = 1

for file in names:
	if file not in complete:
		complete.append(file)
		for file_2 in names:
			bashcommand("dnadiff %s %s -p test_%s" % (file, file_2, test_num))
			snp_file = "test_" + str(test_num) + ".snps"
			snps = getlines(snp_file)
			with open("results.tsv", "a") as fout:
				fout.write("%s\t%s\t%s\n" % (file, file_2, snps))
			test_num += 1

dic = {}
for file in names:
    dic[file] = {}

with open("results.tsv", "r") as fin:
	for line in fin.readlines():
		a = line.split("\t")[0].rstrip()
		b = line.split("\t")[1].rstrip()
		c = line.split("\t")[2].rstrip()
		dic[a][b] = c

#cleanup
os.remove("results.tsv")
for f in glob.glob("test*"):
    os.remove(f)

outfilename = sys.argv[1] + "_results.matrix"
print("results written to = ", outfilename)
df = pd.DataFrame(dic).T
df.to_csv(outfilename, sep='\t')
