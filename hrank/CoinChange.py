#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys

def make_change(numbers, n):
    result = 0
    p=0
    for i in numbers:
        tgt = n 
        t = 0
        while not tgt < 0 :
            t += 1
            tgt = tgt - i
            if tgt == i:
                result += 1
                print((str(i)+'+')*t+str(tgt))
                tgt = -1
            else:
                if tgt in numbers[p:]:
                    result += 1
                    print((str(i)+'+')*t+str(tgt))
            p += 1
    return result

def count(S, n):
 
    m = len(S)
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
        print(table)

    return table[n]

(n,m) = input().strip().split(' ')
ray = [ int(x) for x in input().strip().split(' ')]
print(make_change(ray, int(n)))
print(count(ray, int(n)))


