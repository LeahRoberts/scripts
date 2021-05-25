from Bio import SeqIO
import sys
import os

def define_file(gbk):
    '''
    Edit the output file name
    '''
    name = os.path.splitext(gbk)[0]
    outputname = name + ".fasta"

    return(outputname)


gbk_filename = sys.argv[1]
faa_filename = define_file(gbk_filename)
input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("Dealing with GenBank record %s" % seq_record.id)
    output_handle.write(">%s %s\n%s\n" % (
           seq_record.id,
           seq_record.description,
           seq_record.seq))

output_handle.close()
input_handle.close()
