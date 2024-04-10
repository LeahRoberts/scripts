#!/usr/bin/env python

# script to turn distance matrix into clusters

# Load packages
import pandas as pd
import sys

dist = sys.argv[1] # distance matrix
threshold = sys.argv[2] # threshold for clusters

## load matrix as df:
df = pd.read_csv(dist, sep='\t', header=None)
samples = df[0].tolist()

dic = {}
complete = []
in_cluster = []

cluster_num = 1

for i in range(len(df)):
	idx = df.loc[i,0]
	if idx in in_cluster:
		for key, item in dic.items():
			if key == idx:
				idx_new = item[0]
				for x in range(len(df)):
					matched_position = x - 1
					if matched_position != i: # check it's not the same sample
						comparison_sample = samples[matched_position]
						if comparison_sample not in complete:
							if comparison_sample not in in_cluster:
								distance = df.loc[i, x]
								if int(distance) <= int(threshold):
									dic[idx_new][comparison_sample] = distance
									in_cluster.append(col)
	else:
		complete.append(idx)
		dic[idx] = {}
		for x in range(1, len(df)):
			matched_position = x - 1
			if matched_position != i: # check not comparing same sample
				comparison_sample = samples[matched_position]
				distance = df.loc[i, x]
				if int(distance) <= int(threshold):
					dic[idx][comparison_sample] = distance
					in_cluster.append(comparison_sample)
					in_cluster.append(idx)

#If only want isolates that are clustered, not all singletons
number = 1
for item in dic.items():
	with open("clusters.out", "a") as fout:
		if item[1]:
			cluster = str(item)
			cluster = cluster.strip("(")
			cluster = cluster.strip(")")
			fout.write("cluster_%s\t" % (number))
			fout.write("%s\n" % (cluster))
			number += 1

#if want everything
#number = 1
#for item in dic.items():
#	with open("clusters.out", "a") as fout:
#		cluster = str(item)
#		cluster = cluster.strip("(")
#		cluster = cluster.strip(")")
#		fout.write("cluster_%s\t" % (number))
#		fout.write("%s\n" % (cluster))
#		number += 1

