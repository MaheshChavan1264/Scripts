#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:16:00 2019

@author: root
"""

def problem2_7():
    a = float(input('Enter length of side one: '))
    b = float(input('Enter length of side two: '))
    c = float(input('Enter length of side three: '))
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('Area of a triangle with sides',a,b,c,'is',area)