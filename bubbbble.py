# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:52:56 2018

@author: JerryBruye
"""

a = [5,6,4,2,1,3,8,7,9]
e = ''
for i in range(len(a)):
    for i in range(len(a)-1):
        if int(a[i]) > int(a[i+1]):
            e = a[i]
            a[i] = a[i+1]
            a[i+1] = e
print(a)
    