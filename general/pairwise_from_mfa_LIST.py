from Bio import SeqIO
import sys

# USAGE
# python pairwise_from_mfa.py <multifasta file> <query list> <output_file>
# Script assumes mfa is an alignment i.e. all sequences equal length

def count_SNPs(seq1, seq2):
    #print("counting SNPs...")
    count = sum(1 for a, b in zip(seq1, seq2) if a != b)
    #print(count)
    return(count)

faa_filename = sys.argv[1]
input_handle  = open(faa_filename, "r")

list_in = []
with open(sys.argv[2], "r") as fin:
    for line in fin.readlines():
        line = line.rstrip()
        list_in.append(line)


output_handle = open(sys.argv[3], "a")
completed = []

seq_records = list(SeqIO.parse(input_handle, "fasta"))
for i in range(len(seq_records)):
    subject_id = seq_records[i].id
    subject_seq = seq_records[i].seq
    if subject_id in list_in:
        if subject_id not in completed:
            print("completing", subject_id)
            completed.append(subject_id)
            #print("Handling subject", subject_id)
            for i in range(len(seq_records)):
                query_id = seq_records[i].id
                query_seq = seq_records[i].seq
                if query_id not in completed:
                    #print("Handling query", query_id)
                    snp_number = count_SNPs(subject_seq, query_seq)
                    output_handle.write("%s\t%s\t%s\n" % (subject_id, query_id, snp_number))

input_handle.close()
output_handle.close()
