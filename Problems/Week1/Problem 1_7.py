#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 23:37:41 2019

@author: root
"""

#%%
def problem1_7():
    b1=float(input("Enter the length of one of the bases: "))
    b2=float(input("Enter the length of the other base: "))
    h=float(input("Enter the height: "))
    A = (1/2)*(b1+b2)*h
    print("The area of a trapezoid with bases",b1,"and",b2,"and height",h,"is",A)
#%%