#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import random
import string
import datetime

symbol = 'ы'
symbol = '#'

longstring = ''.join(random.choices(string.ascii_uppercase, k=1000))
longstring += symbol
longdict = { longstring[i]:0 for i in range(len(longstring)) }
shortstring = longstring[:200]
shortstring += symbol
c = longstring[-1]
x = shortstring[-1]

i = 0
start = datetime.datetime.now()
for _ in range(1000000):
    if c in longstring:
        i = i+1
finish = datetime.datetime.now()
print('String in longstring  ' + str(finish-start)+ ' ms')

i=0
start = datetime.datetime.now()
for _ in range(1000000):
    if x in shortstring:
        i = i+1
finish = datetime.datetime.now()
print('String in shortstring ' + str(finish-start)+ ' ms')

i = 0
start = datetime.datetime.now()
for _ in range(1000000):
    if c in longdict:
        i = i+1
finish = datetime.datetime.now()
print('Dict in _____________ ' + str(finish-start)+ ' ms')
