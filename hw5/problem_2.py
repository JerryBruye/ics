#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 15:07:29 2018

@author: dingyuhao
"""

class employee():
    def __init__(self, name, ID, dep, job):
        self.name = name
        self.id = ID
        self.department = dep
        self.job_title = job
    def get_employee(self):
        return self.name, self.id, self.department, self.job_title

Susan = employee('Susan', 47899, 'Accounting', 'vice_president')
Mark = employee('Mark', 39119, 'IT', 'programmer')
Joy = employee('Joy', 81744, 'manufacturing', 'engineer')

print(employee.get_employee(Susan))
print(employee.get_employee(Mark))
print(employee.get_employee(Joy))