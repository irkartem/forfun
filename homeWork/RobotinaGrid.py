#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================

class finder:
    def __init__(self,ray):
            if len(ray) == 0 or len(ray[0])==0:
                return false
            self.mx = ray
    paths = set()
    def print(self):
        for i in range(len(self.mx)):
            print(self.mx[i])

    def nextstep(self,ray,i,j,s=' '):
        s = s+"({},{})->".format(i,j)
        if (i+1) > len(ray):
            return 0
        self.nextstep(ray,i+1,j,s)
        if (j+1) > len(ray[0]):
            return 0
        self.nextstep(ray,i,j+1,s)
        if ray[i][j] == 1:
            return 0
        ray[i][j] = 8
        if i == len(ray)-1 and j == len(ray[0])-1:
  #          print(" {}".format(s))
            self.paths.add(s)
            return 1
#def mxp(ray):
#    for i in range(len(ray)):
#        print(ray[i])
#def nextstep(ray,i,j,s=' '):
#    s = s+"({},{})->".format(i,j)
#    if (i+1) > len(ray):
#        return 0
#    nextstep(ray,i+1,j,s)
#    if (j+1) > len(ray[0]):
#        return 0
#    nextstep(ray,i,j+1,s)
#    if ray[i][j] == 1:
#        return 0
#    ray[i][j] = 8
#    mxp(ray)
#    print(" ")
#    if i == len(ray)-1 and j == len(ray[0])-1:
#        print(" {}".format(s))
#        return 1

w, h = 8, 5
#mx = [[0 for x in range(w)] for y in range(h)] 
mx = [[0]*w for i in range(h)]
mx[2][2] = 1
mx[2][3] = 1
mx[3][2] = 1
mx[3][3] = 1
mx[2][6] = 1
mx[3][6] = 1

sol = finder(mx)
sol.print()
sol.nextstep(mx,0,0,'')
print("\n".join(sol.paths))
#mxp(mx)
#print(nextstep(mx,0,0,s=''))


