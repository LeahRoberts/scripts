#!/usr/bin/env python

# script to cluster resistance genes that are likely in a single MGE from Abricate results

# 1. read in Abricate results file
# 2. get contig - start - end - gene information
# 3. check consecutive lines if:
#     a. gene are on same contig
#     b. end of gene[1] and start of gene[2] within x basepairs
# 4. output contig - start - end - genes for each clustered MGE

# can't really handle circularity yet, because don't have length of contigs information

import sys

ab_results = sys.argv[1]
cutoff = sys.argv[2] if len(sys.argv) >= 3 else 3000

line_num = 0
cluster_num = 0
cluster_genes = {}
cluster_start = {}
cluster_end = {}

with open(ab_results, "r") as f:
    next(f)
    for line in f.readlines():
        if line_num == 0:
            contig = line.split("\t")[1]
            start = line.split("\t")[2]
            end = line.split("\t")[3]
            gene = line.split("\t")[5]
            cluster = "cluster_" + str(cluster_num)
            cluster_genes[cluster] = [gene]
            cluster_start[cluster] = [start]
            cluster_end[cluster] = [end]
            line_num = 1
        elif line_num == 1:
            contig_2 = line.split("\t")[1]
            start_2 = line.split("\t")[2]
            end_2 = line.split("\t")[3]
            gene_2 = line.split("\t")[5]
            if contig == contig_2:
                diff = int(start_2) - int(end)
                if diff < cutoff:
                    cluster_genes[cluster].append(gene_2)
                    cluster_end[cluster] = [end_2]
                    line_num = 2
                else:
                    cluster_num += 1
                    cluster = "cluster_" + str(cluster_num)
                    cluster_genes[cluster] = [gene_2]
                    cluster_start[cluster] = [start_2]
                    cluster_end[cluster] = [end_2]
                    line_num = 2
            else:
                cluster_num += 1
                cluster = "cluster_" + str(cluster_num)
                cluster_genes[cluster] = [gene_2]
                cluster_start[cluster] = [start_2]
                cluster_end[cluster] = [end_2]
                line_num = 2
        elif line_num == 2:
                contig = line.split("\t")[1]
                start = line.split("\t")[2]
                end = line.split("\t")[3]
                gene = line.split("\t")[5]
                if contig == contig_2:
                    diff = int(start) - int(end_2)
                    if diff < cutoff:
                        cluster_genes[cluster].append(gene)
                        cluster_end[cluster] = [end]
                        line_num = 1
                    else:
                        cluster_num += 1
                        cluster = "cluster_" + str(cluster_num)
                        cluster_genes[cluster] = [gene]
                        cluster_start[cluster] = [start]
                        cluster_end[cluster] = [end]
                        line_num = 1
                else:
                    cluster_num += 1
                    cluster = "cluster_" + str(cluster_num)
                    cluster_genes[cluster] = [gene]
                    cluster_start[cluster] = [start]
                    cluster_end[cluster] = [end]
                    line_num = 1

total = cluster_num + 1
for i in range(total):
    cluster = "cluster_" + str(i)
    print("%s\t%s\t%s" % (cluster_start[cluster], cluster_end[cluster], cluster_genes[cluster]))
