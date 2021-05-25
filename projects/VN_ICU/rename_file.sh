#!/bin/bash

INFILE=$1

SAMPLE=$(ls ${INFILE} | cut -f1 -d.)

OUTFILE="${SAMPLE}_filtered.fasta"

mv $INFILE $OUTFILE
