#!/usr/bin/bash

# Take all files in a directory
# count the number of sequences in file
# if file has >=2 sequences, run mafft

[[ -d mafft_align ]] || mkdir mafft_align

for f in *.fa
do
  NAME=$(ls $f | cut -f1 -d.)
  COUNT=$(grep -c ">" $f)
  
  if [ ${COUNT} -ge 2 ]
  then
    mafft --auto $f > ${NAME}.mafft.fa
    mv ${NAME}.mafft.fa mafft_align
  else
    mv $f mafft_align
  fi
done
