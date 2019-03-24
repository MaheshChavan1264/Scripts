#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:15:16 2019

@author: root
"""

def problem3_7(csv_pricefile, flower):
    import csv
    file=open(csv_pricefile)
    for row in csv.reader(file):
        if row[0]==flower:
            print(row[1])