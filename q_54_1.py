# -*- coding:utf-8 -*-
class Solution:

    def isNumeric(self, s):
        try:
            float(s)
            return True
        except:
            return False