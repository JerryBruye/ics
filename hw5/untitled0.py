#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 16:53:16 2018

@author: dingyuhao
"""

class person():
    def __init__(self, address, age, phone):
        self.address = address
        self.age = age
        self.phone = phone
        
Jerry = person('huangpu', 18, 13131313133)

print(Jerry.address)