#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:48:13 2019

@author: root
"""

#%%
import re
temp='indiaparker@ind.com'
temp1=''
if(re.search(r,'@ind\.',temp)):
    temp1=re.sub(r,'i\w+(\.com)',r,'edu\1',temp)
print(temp1)
#%%
f=lambda x: (x*2)%3!=0

def pick(f,list1):
    for item in list1:
        if(not f(item)):
            list1.remove(item)
list=[1,2,3,4,5,6,7,8,9]
pick(f,list)
print(list)
#%%
for i in range(1,6):
    for j in range(1,6):
        if(i%j!=0):
            pass
        elif(j<i):
            continue
        else:
            print(i*j)
#%%
num1=11//10
num2=11%10
num3=20
num4=40
num5=5
if(num3>num4):
    if(num3>num5):
        print(num5*num4/num3)
    else:
        print(num3/num5)
else:
    if(num1==num2):
        print(num4/num3)
    else:
        print(num4/num5)
#%%
i=0
j=10
while i<=10 and j>1:
    print(i,j)
    j=j-1
    i=i+1
    if(i==j):
        break
#%%
        temp="Hello? how are you?"
        if(temp.isdigit()):
            temp+="fine"
        else:
            for i in range(len(temp)):
                if(temp[i]=='?'):
                    finel_val=temp[:i]
                    break
        if(finel_val.endswith('u')):
            final_val.replace('you','u')
        else:
            final_val=final_val.upper()
        print(final_val)