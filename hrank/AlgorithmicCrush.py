#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION: zero array and M operations
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
n, m = (map(int ,input().split(' ')))
erg = [0 for en in range(n)]
ende, added = 0, 0

for q in range(m):
    k1, k2, z = map(int, input().split(' '))
    erg[k1-1] += z
    if k2 < n :
        erg[k2] -= z

print(erg)
for r in erg:
    added += r
    if added > ende:
        ende = added

print(ende)
#(n,m) = map(int,input().strip().split(' '))
#ray = [0] * n
#mx = 0
#
#for i in range(m):
#    (a,b,k) = map(int,input().strip().split(' '))
#    ray[a-1] += k
#    if (mx < ray[l]): mx = ray[l]
#
#print(ray)
#print(mx)
