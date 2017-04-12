#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys
    n = int(input().strip())
    val =list()
    for i in  range(0,n):
        (a,b) = map(int,input().strip().split(' '))
        t = list()
        t.append(a)
        t.append(b)
        val.append(t)
    val.sort()
    
    st = list()
    st.append(val[0])
    for i in val:
        t=st.pop()
        if t[1]<i[0]:
            st.append(t)
            st.append(i)
        if t[1]>i[0]:
            t[1] = i[1]
            st.append(t)
    print(len(st))
    for i in range(len(st)):
        t = st.pop()
        print("{} {}".format(t[0],t[1]))



