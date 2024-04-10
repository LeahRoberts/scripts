import json
import sys

gene_hits = sys.argv[1]
samples = sys.argv[2]

y = open(gene_hits)
data = json.load(y)

with open(samples, "r") as fin:
	for name in fin.readlines(): 
		name = name.rstrip()
		outfilename = name + "_genes.txt"
		with open(outfilename, "a") as fout:
			for i in data[name]:
				fout.write("%s\n" % (i))
		fout.close()
	fin.close()	



