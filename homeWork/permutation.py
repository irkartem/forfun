#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================

def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

def checkPR(ray):
    lst = []
    for c in ray:
        if c == '(':
            lst.append(c)
        if c == ')':
            if len(lst) < 1 or lst.pop() != "(":
                return False
    return True

ar = ['a','c','c','n','w'];
ar = ['(','(','(','(',')',')',')',')'];

if checkPR(ar): print ("".join(ar));
while next_permutation(ar):
    if checkPR(ar): print ("".join(ar));

