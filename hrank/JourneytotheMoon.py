#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
from math import factorial
n,p = map(int,input().strip().split(' '))
cnt = []
mset = set([i+1 for i in range(0,n-1)])
while p>0:
    p -= 1
    a,b = map(int,input().strip().split(' '))
    new = True
    for k in cnt:
        if a in k:
            k.add(b)
            mset -= set([b])
            new = False
        if b in k:
            k.add(a)
            mset -= set([a])
            new = False
# create new set in array
    if new: 
        tmp = set([a,b])
        mset -= set([a,b])
        cnt.append(tmp)

for tmp in mset:
    cnt.append(set([tmp]))

npos = 0
possible = factorial(n)/(factorial(n-2)*2)
for i in range(0,len(cnt)):
    for k in range(i+1,len(cnt)-1):
        if len(cnt[i].intersection(cnt[k])) >0:
            cnt[i].update(cnt[k])
            cnt.pop(k)
for i in range(0,len(cnt)):
    curlen = len(cnt[i])
    if curlen>1:
        possible -= factorial(curlen)/(factorial(curlen-2)*2)

print(cnt)
print(int(possible))
