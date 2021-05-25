#!/usr/bin/env python

# script to turn distance matrix into clusters

# Load packages
import pandas as pd
import sys

dist = sys.argv[1] # distance matrix
threshold = sys.argv[2] # threshold for clusters

## load matrix as df:
df = pd.read_csv(dist, sep='\t', header=0)

new_columns = df.columns.values
new_columns[0] = 'axis1'
df.columns = new_columns
df = df.set_index('axis1') # set the first column as the index

dic = {}
complete = []
in_cluster = []

for i in range(len(df)):
	idx = df.index[i]
	if idx in in_cluster:
		complete.append(idx)
		for item in dic.items():
			for key in item:
				if idx in key:
					idx_new = item[0]
					for i in range(len(df)):
						col = df.columns[i]
						if col != idx: # check it's not the same sample
							if col not in complete:
								if col not in in_cluster:
									distance = df.loc[idx, col]
									if int(distance) <= int(threshold):
										dic[idx_new][col] = distance
										in_cluster.append(col)
	else:
		complete.append(idx)
		dic[idx] = {}
		for i in range(len(df)):
			col = df.columns[i]
			if col != idx: # check it's not the same sample
				if col not in complete:
					if col not in in_cluster:
						distance = df.loc[idx, col]
						if int(distance) <= int(threshold):
							dic[idx][col] = distance
							in_cluster.append(col)

#If only want isolates that are clustered, not all singletons
# number = 1
# for item in dic.items():
# 	with open("clusters.out", "a") as fout:
# 		if item[1]:
# 			cluster = str(item)
# 			cluster = cluster.strip("(")
# 			cluster = cluster.strip(")")
# 			fout.write("cluster_%s\t" % (number))
# 			fout.write("%s\n" % (cluster))
# 			number += 1

#if want everything
number = 1
for item in dic.items():
	with open("clusters.out", "a") as fout:
		cluster = str(item)
		cluster = cluster.strip("(")
		cluster = cluster.strip(")")
		fout.write("cluster_%s\t" % (number))
		fout.write("%s\n" % (cluster))
		number += 1