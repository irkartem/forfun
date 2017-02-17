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

print(make_change([1,2,3], 4))




