# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:45:32 2018

@author: JerryBruye
"""

a = open("WorldSeriesWinners.txt",'r')
b = a.read()
b = b.split('\n')
c = input("Team names:")
for i in b: