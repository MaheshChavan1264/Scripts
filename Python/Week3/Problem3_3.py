#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:45:13 2019

@author: root
"""

def problem3_3(month, day, year):
    m={"1":"January","2":"February","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}
    print(m[str(month)],str(day)+",",year)