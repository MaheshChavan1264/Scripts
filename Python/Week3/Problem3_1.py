#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:42:20 2019

@author: root
"""

def problem3_1(txtfilename):
    file=open(txtfilename,"r")
    chars=0
    print(file.read(),end="")
    print()
    print()
    file.close()
    file=open(txtfilename,"r")
    for line in file:
        chars=chars+len(line)
    print
    print("There are",chars,"letters in the file.")
    file.close()
