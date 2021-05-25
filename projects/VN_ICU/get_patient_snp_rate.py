#!/usr/bin/env python

import sys
import glob
import datetime
import subprocess
from subprocess import CalledProcessError
import os
import re

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

#import files

# metadata file should have dates already sorted from earliest to latest
# contains IsolateID, patientID, date and ST
# Should have "L[0-9]" removed
# Patients = non-redundant list of patient IDs
patients = sys.argv[1]
metadata = sys.argv[2]
snpdist = sys.argv[3]

with open(patients, "r") as fin:
    for p in fin.readlines():
        patient = p.rstrip()
        bashcommand("grep -w %s %s > temp.txt" % (patient, metadata))
        # Need to sort into temp files for each specific ST
        bashcommand("cut -f4 temp.txt | sort | uniq > ST.txt")
        with open("ST.txt", "r") as sin:
            for num in sin.readlines():
                num = num.rstrip()
                outname = num + ".temp"
                bashcommand("grep -w %s temp.txt > %s" % (num, outname))
        # now want to open each ST specific file and count SNP distances
        in_files = glob.glob('*.temp')
        for f in in_files:
            with open(f, "r") as tin:
                count = 1
                for line in tin.readlines():
                    if count == 1:
                        index = line.split("\t")[0]
                        date = line.split("\t")[2]
                        day,month,year = date.split("/")
                        idate = datetime.date(int(year),int(month),int(day))
                        iST = line.split("\t")[3].rstrip()
                        bashcommand("grep -w %s %s > snps.tmp" % (index, snpdist))
                        count +=1
                    else:
                        sample = line.split("\t")[0]
                        date = line.split("\t")[2]
                        day,month,year = date.split("/")
                        sdate = datetime.date(int(year),int(month),int(day))
                        date_dif = sdate - idate
                        with open("snps.tmp") as sin:
                            for line in sin.readlines():
                                if sample in line:
                                    dist = line.split("\t")[2].rstrip()
                        with open("patient_dist_summary.tsv", "a") as fout:
                            fout.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (patient, index, sample, date_dif, dist, iST))

        filelist = [ f for f in os.listdir("./") if f.endswith(".temp") ]
        for f in filelist:
            os.remove(os.path.join("./", f))


os.remove("temp.txt")
os.remove("ST.txt")
os.remove("snps.tmp")
