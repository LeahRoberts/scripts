import sys
import pandas as pd

genes = sys.argv[1] # gene matrix

geneDf = pd.read_csv(genes, sep='\t', header=0) # make df from gene matrix
new_columns = geneDf.columns.values
new_columns[0] = 'genes'
geneDf.columns = new_columns
geneDf = geneDf.set_index('genes') # set the first column as the index

samples = (list(geneDf)[0:]) # get column headers as list

core = len(samples) # total number of samples

geneDf['Total'] = geneDf.sum(axis=1)

core_geneDf = geneDf[(geneDf == int(core)).any(axis=1)]

outfilename = "core_genes.tsv"
print("results written to = ", outfilename)
core_geneDf.to_csv(outfilename, sep='\t')