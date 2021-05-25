#!/usr/bin/perl
#usage: filterSpadesAss.pl <input> <min_contig_coverage[INT]> <min_contig_length[INT]>

use strict;
use Bio::SeqIO;

my $input = $ARGV[0];
my $cov = $ARGV[1];
my $len = $ARGV[2];

my $test = system("echo $input");

my $process = system("grep -F '>' $input | sed -e 's/_/ /g' |sort -nrk 6 |awk '\$6>=$cov && \$4>=$len {print \$0}'| sed -e 's/ /_/g'|sed -e 's/>//g'>$input.txt");
my $filter = system("~/bin/fastagrep.pl -f $input.txt $input > $input.filtered");
