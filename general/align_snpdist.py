#!/usr/bin/env python

# script to align sequences with mauve, run snp-sites and then snp-dists
# must have snpsites and snpdist in path
# check that paths to harvesttools and mauve are correct

import sys
import subprocess
from subprocess import CalledProcessError
import glob
import os

def listToString(s):
    str1 = " "
    return (str1.join(s))


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


file_path = sys.argv[1] + "/*" # folder containing sequences

names = []

for file in glob.glob(file_path):
	names.append(file)
	sml_file = file + ".sml"
	names.append(sml_file)

print("Running mauve...")
bashcommand("/Applications/Mauve.app/Contents/MacOS/mauveAligner --output-alignment=%s.xmfa %s" % (sys.argv[1], listToString(names)))
print("running harvesttools...")
bashcommand("~/bin/harvesttools-OSX64-v1.2/harvesttools -x %s.xmfa -M %s.mfa" % (sys.argv[1], sys.argv[1]))
print("running snpsites...")
bashcommand("snp-sites -o %s_snps.mfa %s.mfa" % (sys.argv[1], sys.argv[1]))
print("running snpdist...")
bashcommand("snp-dists %s.mfa > %s_distances.matrix" % (sys.argv[1], sys.argv[1]))
