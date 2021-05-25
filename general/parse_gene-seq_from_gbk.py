#!/usr/bin/env python

from Bio import SeqIO
import sys
import os


def define_file(gbk):
    '''
    Edit the output file name
    '''
    name = os.path.splitext(gbk)[0]
    outputname = name + "_genes.fasta"

    return(outputname)


gbk_filename = sys.argv[1]
faa_filename = define_file(gbk_filename)
input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("Dealing with GenBank record %s" % seq_record.id)
    for feature in seq_record.features:
        if feature.type == "gene":
            feature_name = feature.qualifiers["locus_tag"][0]
            feature_seq = feature.extract(seq_record.seq)
            output_handle.write(">%s\n%s\n" % (feature_name, feature_seq))

output_handle.close()
input_handle.close()
