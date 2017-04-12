#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys

def get_all(string):
    length = len(string)
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            yield(string[i:j]) 

for i in get_all("abcde"):
    print(i)
