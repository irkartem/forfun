#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys

def avg(l):
        return sum(l, 0.0) / len(l)

n = int(input().strip())
hs = dict()
for i in  range(0,n):
    (iht,r) = map(int,input().strip().split(' '))
    if hs.get(iht):
       hs[iht].append(r)
    else:
        hs[iht] = list()
        hs[iht].append(r)

for k in hs.keys():
   av = avg(hs[k]) 
   hs[k] = av

s = [(k, hs[k]) for k in sorted(hs, key=hs.get, reverse=True)]
print(s)
for k, v in s:
    print(k)
