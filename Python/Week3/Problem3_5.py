#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:53:30 2019

@author: root
"""

def problem3_5(name):
    """ Looks up the phone number of the person whose name is name """
    
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241", \
                      "james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    print(phone_numbers[name])