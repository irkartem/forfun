#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
def issubstr(fst,scd):
    ray = list(fst)
    for l in list(scd):
        print(ray)
        try: 
            ray.remove(l)
        except ValueError:
                pass  # do nothing!
    if len(ray) > 0 : return False 
    else: return True

import unittest
class TestAngramm(unittest.TestCase):

      def test_upper(self):
                self.assertTrue(issubstr('ping', 'jinpg'))
                self.assertTrue(issubstr('piiiing', 'ijinipgi'))
                self.assertTrue(issubstr('ping', 'ping'))
                self.assertTrue(issubstr('', 'jinpg'))
                self.assertTrue(issubstr('p', 'p'))
                self.assertFalse(issubstr('pp', 'p'))
                self.assertFalse(issubstr('pap', 'ppp'))

if __name__ == '__main__':
    unittest.main()
