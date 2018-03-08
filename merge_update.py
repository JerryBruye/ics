# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:29:27 2018

@author: JerryBruye
"""


def nlog(arr):

	if len(arr)<=1:
		return arr
	mid = len(arr)//2
	left_arr = nlog(arr[:mid])
	right_arr = nlog(arr[mid+1:])
	return merge(left_arr,right_arr)
def merge(a,b):
	result = []
	i,j = 0,0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			result.append(a[i])
			i +=1
		else:
			result.append(b[j])
			j += 1
	if i == len(a):
		for k in b[j:]:
			result.append(k)
	else:
		for k in a[i:]:
			result.append(k)
	return result
list1 = [1,4,6,9]
list2 = [2,3,5,10]
print(merge(list1,list2))
arr = [4,6,4,2,4,56,7,8,2,23,5]
print(nlog(arr))