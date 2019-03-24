#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:53:43 2019

@author: root
"""

def extend_name():
    fname=input("Enter your first name: ")
    lname=input("Enter your last name: ")
    cname=input("Enter the city name: ")
    sname=input("Enter the state name: ")
    fullname=fname + " " + lname
    print("Your full name is: ",fullname)
    live_in=cname + "," + sname
    print("Your live in: ",live_in)