#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
def canpalindrome(str):
    dct = {}

    for c in str:
        if dct.get(c):
            dct[c] -= 1
        else: dct[c] = 1
    onecnt = 0
    for i in dct:
        if dct[i] == 1:
            onecnt += 1
    if len(str) % 2 == 0 and onecnt < 3:
        return True
    if len(str) % 2 != 0 and onecnt == 1:
        return True
    return False

import unittest
class Test(unittest.TestCase):

      def test_pali(self):
                self.assertTrue(canpalindrome('tactca'))
                self.assertTrue(canpalindrome('tac toca'))
                self.assertTrue(canpalindrome('tac tca'))
                self.assertFalse(canpalindrome('tac tdfa'))

if __name__ == '__main__':
    unittest.main()
