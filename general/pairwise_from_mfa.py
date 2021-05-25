from Bio import SeqIO
import sys
import pandas as pd

# USAGE
# python pairwise_from_mfa.py <multifasta file> > output_file.txt
# Script assumes mfa is an alignment i.e. all sequences equal length

def count_SNPs(seq1, seq2):
    #print("counting SNPs...")
    count = sum(1 for a, b in zip(seq1, seq2) if a != b)
    #print(count)
    return(count)

faa_filename = sys.argv[1]
input_handle  = open(faa_filename, "r")

#completed = []
dic = {}

seq_records = list(SeqIO.parse(input_handle, "fasta"))
for i in range(len(seq_records)):
	subject_id = seq_records[i].id
	dic[subject_id] = {}
	subject_seq = seq_records[i].seq
	#if subject_id not in completed:
	#completed.append(subject_id)
	#print("Handling subject", subject_id)
	for i in range(len(seq_records)):
		query_id = seq_records[i].id
		query_seq = seq_records[i].seq
		#if query_id not in completed:
		#print("Handling query", query_id)
		snp_number = count_SNPs(subject_seq, query_seq)
		dic[subject_id][query_id] = snp_number
		#print("%s\t%s\t%s" % (subject_id, query_id, snp_number))

outfilename = "distance.matrix"
print("results written to = ", outfilename)
df = pd.DataFrame(dic)
df.to_csv(outfilename, sep='\t')

input_handle.close()

