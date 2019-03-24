#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:18:28 2019

@author: root
"""
a=int(input("enter the starting number: "))
b=int(input("enter the ending number: "))

even=[]
odd=[]
for n in range(a,b):
    if n%2==0:
        even.append(n)
    else:
         odd.append(n)
print("Even numbers:",even)
print("Odd numbers:",odd)
