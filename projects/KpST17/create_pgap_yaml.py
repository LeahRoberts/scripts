#!/usr/bin/env python

import sys
import re

handle = sys.argv[1]

outfile = re.sub(r"\.\w+$", r".input.yaml", handle)


'''
fasta:
  class: File
  location: KN_0056A-F_assembly.modified.fa
submol:
  class: File
  location: submol.yaml
'''

with open(outfile, "w") as fout:
	fout.write("fasta:\n")
	fout.write("  class: File\n")
	fout.write("  location: %s\n" % (handle))
	fout.write("submol:\n")
	fout.write("  class: File\n")
	fout.write("  location: submol.yaml\n")


