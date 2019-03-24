#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 23:15:56 2019

@author: root
"""

#%%
def problem1_5(age):
    if age < 7:
        print("Have a glass of milk.")
    elif (age > 7) & (age < 21):
        print("Have a coke.")
    else:
        print("Have a martini.")
#%%