#!/usr/bin/env python

import sys
import subprocess
from subprocess import CalledProcessError
import glob
import os

# Simple script for finding basic SNP rate in patients
# Take two isolates from same patient with greatest SNP difference
# Divide SNPs/days to get rate

patients = sys.argv[1]
snp_file = sys.argv[2]

def bashcommand(command):
	'''
	Execute a shell command by concatenating a string
	and executing using subprocesses
	'''

	with open("command_log.txt", "a") as fout:
		fout.write("%s\n" % command)

	try:
		subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except CalledProcessError as e:
		print(e.output)



with open(patients, "r") as pin:
    for pat in pin.readlines():
        pat = pat.rstrip()
        bashcommand("grep -w %s %s > temp.txt" % (pat, snp_file))
        # Need to divide into STs again
        bashcommand("cut -f6 temp.txt | sort | uniq > ST.txt")
        with open("ST.txt", "r") as sin:
            for num in sin.readlines():
                num = num.rstrip()
                outname = num + ".temp"
                bashcommand("grep -w %s temp.txt > %s" % (num, outname))
            in_files = glob.glob("*.temp")
            for f in in_files:
                bashcommand("sort -k5 -n -r %s | head -1 > out.txt" % (f))
                with open("out.txt", "r") as x:
                    for line in x.readlines():
                        p = line.split("\t")[0]
                        d = line.split("\t")[3]
                        snp = line.split("\t")[4]
                        st = line.split("\t")[5].rstrip()
                        with open("basic_SNP_dist_summary.tsv", "a") as fout:
                            fout.write("%s\t%s\t%s\t%s\n" % (p, st, snp, d))

            filelist = [ f for f in os.listdir("./") if f.endswith(".temp") ]
            for f in filelist:
                os.remove(os.path.join("./", f))

os.remove("out.txt")
os.remove("temp.txt")
os.remove("ST.txt")
