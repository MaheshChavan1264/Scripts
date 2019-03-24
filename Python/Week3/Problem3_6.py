#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:01:11 2019

@author: root
"""

import sys
infile=sys.argv[1]
outfile=sys.argv[2]
readfile=open(infile)
writefile=open(outfile,"w")
for line in readfile:
    line=line.strip("\n")
    writefile.write(str(len(line)))
    writefile.write("\n")
readfile.close()
writefile.close()


