#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:38:01 2019

@author: root
"""

def problem2_2(my_list):
    print(my_list)
    print(my_list[0])
    n=len(my_list)
    print(my_list[n-1])
    print(my_list[3:5])
    print(my_list[0:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append('z')
    print(my_list)