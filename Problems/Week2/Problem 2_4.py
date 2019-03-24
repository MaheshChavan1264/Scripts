#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:28:45 2019

@author: root
"""
import random

def problem2_4():

    random.seed(70)
    list_no=[]
    i = 0
    while(i<10):
        x = (5*random.random()+30)
        list_no.append(x)
        i=i+1
    print(list_no)   
       
        