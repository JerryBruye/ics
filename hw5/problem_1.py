#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:57:55 2018

@author: dingyuhao
"""

def summ(a):
    if len(a) == 1:
        return a[0]
    return a[0] + summ(a[1:])

print(summ([1,2,3,4,5,6,7,8,9,10]))