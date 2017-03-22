#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
def count(ray, n):
    table = [0 for k in range(n+1)]
    #first case 0 value
    table[0] = 1
    for i in range(0,len(ray)):
        for j in range(ray[i],n+1):
            table[j] += table[j-ray[i]]
    return table[n]

arr = [5, 10,20,25]
n = 100
x = count(arr, n)
print (x)

