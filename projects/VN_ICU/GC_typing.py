#!/usr/bin/env python

import glob

in_files = glob.glob('*out')

for f in in_files:
    with open(f, "r") as fin:
        line_count = 0
        IC1 = 0
        IC2 = 0
        for line in fin.readlines():
            line_count += 1
            if "IC1" in line:
                IC1 += 1
            elif "IC2" in line:
                IC2 += 1
        if IC1 >0 and IC2==0:
            with open("output_summary.txt", "a") as fout:
                fout.write("%s\t%s\tIC1\n" %(f,line_count))
        elif IC1==0 and IC2 >0:
            with open("output_summary.txt", "a") as fout:
                fout.write("%s\t%s\tIC2\n" %(f,line_count))
        elif IC1>0 and IC2>0:
            with open("output_summary.txt", "a") as fout:
                fout.write("%s\t%s\tBOTH\n" %(f,line_count))            
        else: #no hits
            with open("output_summary.txt", "a") as fout:
                fout.write("%s\t%s\tnone\n" %(f,line_count))
