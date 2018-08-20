# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.adict = {}
        self.alist = []
    def FirstAppearingOnce(self):
        # write code here
        for i in self.adict:
            if self.adict[i] = 1:
                return i
        return "#"

    def Insert(self, char):
        # write code here
        # alist.append(char)
        if char not in self.adict.keys():
            self.adict[char] = 1
        else:
            self.adict[char] += 1