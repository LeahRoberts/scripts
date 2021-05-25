#!/usr/bin/env bash

FILE=$1

SAMPLE_1=$(cut -f1,3 ${FILE} | head -2 | tail -1)
SAMPLE_2=$(cut -f1,3 ${FILE} | head -3 | tail -1)

echo -e "${SAMPLE_1}\n${SAMPLE_2}" >> aligned_based_summary.txt
