#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:02:58 2019

@author: root
"""

import random

def problem2_5():
    random.seed(171)  # don't remove when you submit for grading
    for roll in range(0,10):
        print(random.randint(1,6))