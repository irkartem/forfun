#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================

n = input().strip()

ray = [int(i) for i in str(n)]

bindex = 0
possible = 0
for i in range(1,len(ray)):
    if ray[i-1] < ray[i]: possible = 1
    if ray[i] > ray[bindex]: 
        bindex = i
if possible > 0:
    for i in range(bindex):
        if ray[i] < ray[bindex]:
            ray[i],ray[bindex] = ray[bindex],ray[i]
            break
    print(ray)
else:
    print("Not possible {}".format(n))
