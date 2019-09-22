# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:45:48 2018

@author: fa15-bse-014
"""

l=[3,4,5,6]
l2=[]
for i in l:
    l2.append(i**0.5)
    print(l2)
    print("")
for i in l:
    l2.append(i**3)
    print(l2)

l3=[1,4,"jamal",8]
l1=[i**2 for i in l if i%2!=0]
print(l1)
l3=[i**2 for i in l3 if type(i)!=str]
print(l1)