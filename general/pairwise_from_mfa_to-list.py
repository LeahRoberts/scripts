from Bio import SeqIO
import sys
import pandas as pd

# USAGE
# python pairwise_from_mfa.py <multifasta file> > outputfile.txt
# Script assumes mfa is an alignment i.e. all sequences equal length

def count_SNPs(seq1, seq2):
    #print("counting SNPs...")
    count = sum(1 for a, b in zip(seq1, seq2) if a != b)
    #print(count)
    return(count)

faa_filename = sys.argv[1]
input_handle  = open(faa_filename, "r")

completed = []

seq_records = list(SeqIO.parse(input_handle, "fasta"))
for i in range(len(seq_records)):
	subject_id = seq_records[i].id
	subject_seq = seq_records[i].seq
	if subject_id not in completed:
		completed.append(subject_id)
		for i in range(len(seq_records)):
			query_id = seq_records[i].id
			query_seq = seq_records[i].seq
			if query_id not in completed:
				snp_number = count_SNPs(subject_seq, query_seq)
				print("%s\t%s\t%s\n" % (subject_id, query_id, snp_number))


input_handle.close()
