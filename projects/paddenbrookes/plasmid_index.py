#!/usr/bin/env python

# script to compare plasmid index to sample matrix (both output from Pandora)
# and determine which plasmids (from the index) are likely present in the samples

import sys
import numpy as np
import pandas as pd
import csv
import os

index = sys.argv[1] # plasmid index
sample = sys.argv[2] # sample matrix

indexDf = pd.read_csv(index, sep='\t', header=0)
sampleDf = pd.read_csv(sample, sep='\t', header=0)

plasmids = (list(indexDf)[1:]) # get column headers as list
samples = (list(sampleDf)[1:])

#Merge two datasets
merge = pd.merge(indexDf, sampleDf, on=['genes'], how='left')

# sum the total for each plasmid in the index:
total = {}
for p in plasmids:
    total[p] = int(merge[p].sum())

dic = {}
for s in samples:
    dic[s] = {}
    merge[s] = merge[s].replace(0, np.nan)
    for p in plasmids:
        # compare each sample column to each plasmid column
        comparison = np.where(merge[p] == merge[s], 1, 0)
        sum = np.sum(comparison)
        dic[s][p] = float(int(sum)/int(total[p]))*100

outfilename = "results.csv"
print("results written to = ", outfilename)
df = pd.DataFrame(dic).T
df.to_csv(outfilename, sep='\t')
