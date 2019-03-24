#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:02:24 2019

@author: root
"""
import random

def problem2_6():
    random.seed(431)  # don't remove when you submit for grading
    for roll in range(0,100):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(die1+die2)
   
        