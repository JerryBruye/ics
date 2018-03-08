#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:27:32 2018

@author: dingyuhao
"""

class employee:
    def __init__(self):
        self.info = {"name":self}
    def name(self):
        self.info["name"] = self
    def idn(self, idn):
        self.info["ID"] = idn
    def dep(self, dep):
        self.info["department"] = dep
    def job(self, job):
        self.info['job_title'] = job
    def get_employee(self):
        return self.info
    def add(self):
        ID = input("ID:")
        dep = input("Department")
        job = input("Job_title:")
        self.info["name"] = self
        self.info["ID"] = idn
        self.info["department"] = dep
        self.info['job_title'] = job
    
print("1. Look up an employee in the dictionary\n\
2. Add a new employee to the dictionary\n\
3. Change an existing employee’s name, department, and the job title in the dictionary\n\
4. Delete an employee from the dictionary\n\
5. Quit the program")    
num = int(input("Please enter the number:"))