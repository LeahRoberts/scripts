import json
import sys

'''
Run like this: 
python parse_json.py json_file list_of_samples

produces a file for each sample that lists the genes it hit
'''

gene_hits = sys.argv[1]
samples = sys.argv[2]

y = open(gene_hits)
data = json.load(y)

with open(samples, "r") as fin:
	for name in samples.readlines(): 
		name = name.rstrip()
		outfilename = name + "_genes.txt"
		with open(outfilename, "a") as fout:
			for i in data[name]:
				fout.write("%s\n" % (i))
		fout.close()
	fin.close()	

