#!/usr/bin/env python

import sys

p_call_complete = []
p_call_dic = {}

type_dic = {}
type_complete = []

with open("log.txt", "a") as log:
	log.write("Starting to parsing probe results per panvar\n")

with open("ALL_probes.bed", "r") as fin:
	for line in fin:
		type = line.split(" ")[0].rstrip() # genic or intergenic
		desc = line.split("\t")[3].rstrip()
		id = desc.split("_")[0].rstrip() #panvar id
		p_call = desc.split("_")[1].rstrip() #pandora call (true or false)
		
		# dic to record true/false calls from Pandora with panvar ID:
		if id in p_call_complete:
			p_call_dic[id].append(p_call)
		else:
			p_call_dic[id] = [p_call]
			p_call_complete.append(id)
			
		# dic to record gene/intergenic call from bedtools intersect:
		
		if id in type_complete:
			type_dic[id].append(type)
		else:
			type_dic[id] = [type]
			type_complete.append(id)

with open("log.txt", "a") as log:
	log.write("finished parsing probes\n")
	log.write("starting merge of panvar pandora calls and bedtools intersects\n")
#p_call_dic:
#{'probe1': [true, false, false, true]}
#type_dic:
#{'probe1': [intergenic, intergenic, intergenic, intergenic]}
# merge information from the two dictionaries

keys = list(p_call_dic.keys())
with open("panvar_summary.tsv", "a") as fout:
	fout.write("%s\t%s\t%s\t%s\t%s\n" % ("panvarID", "#genomes", "type", "true", "false"))
	for panvar in keys:
		calls = p_call_dic[panvar] #[true, false, true, false]
		nb_of_samples = len(calls)
		false = calls.count('False')
		true = calls.count('True')
		tmp = type_dic[panvar] #list of genic or intergenic probes
		result = all(x == tmp[0] for x in tmp)
		if result is True:
			type = tmp[0]
		else:
			type = 'mix'
		fout.write("%s\t%s\t%s\t%s\t%s\n" % (panvar, nb_of_samples, type, true, false))

with open("log.txt", "a") as log:
	log.write("finished!\n")

