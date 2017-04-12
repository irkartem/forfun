#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys
import itertools


sray= set(input().strip())

view = set()
for i in range(0, len(sray) + 1):
    for tmp in itertools.permutations(sray, i):
        for k in tmp:
            t = t + (str(k))
            view.add(''.join(sorted(t)))
        t = ""
for i in view:
    print(i)
