#! usr/bin/bash 

INFILE=$1

echo mean, max, min

cat $INFILE | awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}; if($1<min) {min=$1}; total+=$1; count+=1} END {print total/count, max, min}'

echo median

sort -n $INFILE | awk ' { a[i++]=$1; } END { print a[int(i/2)]; }'
