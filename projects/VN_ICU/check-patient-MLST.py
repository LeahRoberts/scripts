#!/usr/bin/env python

import sys
import re
import os

#input --> non-redundant list of patient IDs and STs (tab delimited, species specific)
#patient ID list --> list of patient IDs (without L number)

def count_file_lines(file):
    num_lines = sum(1 for line in open(file))
    return(num_lines)

patients = open(sys.argv[1], "r")

carriage = []
change = []
L1_only = []
acquired = []

for id in patients.readlines():
    id = id.rstrip()
    id_list = []
    with open(sys.argv[2], "r") as mlst:
        for line in mlst.readlines():
            if id in line:
                with open("temp.txt", "a") as fout:
                    fout.write(line)

        levels = count_file_lines("temp.txt")
        if levels > 1:
            with open("temp.txt", "r") as fin:
                for lines in fin.readlines():
                    L_number = lines.split("\t")[0].rstrip()
                    L_number = L_number.split("L")[1]
                    patient_L = id + "L" + L_number
                    ST = lines.split("\t")[1].rstrip()
                    id_list.append(ST)
            result = all(elem == id_list[0] for elem in id_list)
            if result:
                carriage_id = id + "_" + id_list[0]
                carriage.append(carriage_id)
            else:
                change_id = str("_".join(map(str, id_list)))
                change_id = id + "_" + change_id
                change.append(change_id)
        elif levels == 1:
            with open("temp.txt", "r") as fin:
                for line in fin.readlines():
                    ST = line.split("\t")[1].rstrip()
                    name = id + "_" + ST
                    if "L1" in line:
                        L1_only.append(name)
                    else:
                        acquired.append(name)
        else:
            print("no lines in file - check", id)
            exit()

        os.remove("temp.txt")


with open("carriage.txt", 'w') as p:
	for item in carriage:
		p.write("%s\n" % item)

with open("change_ST.txt", 'w') as x:
	for item in change:
		x.write("%s\n" % item)

with open("L1_only.txt", 'w') as r:
	for item in L1_only:
		r.write("%s\n" % item)

with open("acquired.txt", 'w') as z:
	for item in acquired:
		z.write("%s\n" % item)
