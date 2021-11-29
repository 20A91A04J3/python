# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:55:41 2021

@author: sys18
"""
n = int(input("enter array length:"))
arr = input("enter array elements:")  
l = list(map(int,arr.split(' ')))

b= list(set(l))
print(b)
