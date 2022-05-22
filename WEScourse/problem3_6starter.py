# -problem3_6.py *- coding: utf-8 -*-

import sys

infilename = sys.argv[1]
outfilename = sys.argv2[2]

infile = open(infilename)
outfile = open(outfilename, "w")

for line in infile:
    line.strip("\n")
    outfile.write (len(line))

infile.close()
outfile.close()

