#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys

def getmaxprofit(ray):
    result=0
    for i in range(len(ray)-1):
        for l in range(i+1,len(ray)):
                if result < ray[i]-ray[l]:
                    result = ray[i]-ray[l]
    return result

stockYesterday =[10,7,5,8,11,9]

print(getmaxprofit(stockYesterday))

