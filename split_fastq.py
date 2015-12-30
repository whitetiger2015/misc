#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import gzip
import math

def check_fastq_read_num(infile_split):
    stream_infile_split = gzip.open(infile_split, 'r')
    line_num = 0
    line = stream_infile_split.readline()
    while line:
        line_num = line_num + 1
        line = stream_infile_split.readline()
    print "line_num = " + str(line_num)
    if line_num % 4 != 0:
        print "line_num " + str(line_num) + " is not a multiple of 4."
    else:
        read_num = line_num / 4
    return read_num

def split_fastq(infile_split, outfile_split, read_num):
    #read_size_per_file = 1000000
    read_size_per_file = 1000
    if read_num % read_size_per_file == 0:
        file_num = read_num / read_size_per_file
    else:
        file_num = math.ceil(float(read_num) / read_size_per_file)
    print "file_num = " + str(int(file_num))
    file_names = []
    for i in range(0, int(file_num)):        
        file_names.append("output_" + str(i + 1) + ".txt")
    for i in range(0, int(file_num)):        
        print "file_names[" + str(i) + "] = " + file_names[i]




    ret = 0
    print "ret = " + str(ret)
    return ret


if __name__ == "__main__":

    infile = sys.argv[1]
    infile_base = infile.replace(".fastq.gz", "")
    infile_split = infile
    outfile_split = infile_base
    print infile
    stat = 0
    read_num = 0
    read_num = check_fastq_read_num(infile_split)
    print "read_num = " + str(read_num)
    if stat == 0:
        stat = split_fastq(infile_split, outfile_split, read_num)
        pass
    else:
        print "Error in check_fastq_read_num."
        exit
    print "--------------------------------------------"
