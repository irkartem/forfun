#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
a,b,n = map(int,input().strip().split(' '))
ray = []
ray.append(a)
ray.append(b)
i = 2
while (i < n):
       ray.append(ray[i-2] + (ray[i-1] * ray[i-1]))
       i += 1
print(ray[n-1])

