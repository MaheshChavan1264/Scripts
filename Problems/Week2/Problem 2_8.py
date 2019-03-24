#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:08:37 2019

@author: root
"""
def problem2_8(temp_list):
    sum_=0
    for i in range(0,len(temp_list)):
        sum_=sum_+temp_list[i]
    average=sum_/len(temp_list)
    print("Average:",average)
    m=max(temp_list)
    n=min(temp_list)
    print("High:",m)
    print("Low:",n)
    

