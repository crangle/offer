# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # 1.s的当前字符是否与pattern当前字符匹配
            # ？如何取string的单个字符 s[0]
        # 2.若不匹配，则直接返回false
        # 3.若匹配，继续下一个字符
        if not s:
            if pattern:
                if len(pattern) > 2:
                    if pattern[1] == '*':
                        return self.match(s,pattern[i+2:])
                elif len(pattern) == 2:
                    return pattern[1] == '*'
                else:
                    return False
            else:
                return True
        if s and not pattern:
            return False
        if len(s) == 1 and len(pattern) == 1:
            return s[0] == pattern[0] or pattern[0] == '.'
        i = 0
        if s and pattern:
            #print(s[0],pattern[0])
            if pattern[i] == s[i] or pattern[i] == '.':
                # 若当前匹配,且pattern下一个为'*'
                if pattern[i+1] == '*':
                    return self.match(s[i+1:],pattern[i:])
                # if len(s) == 1 and len(pattern) == 1:
                #     return True
                # if len(s) == 1 and len(pattern) > 1:
                #     self.match[[],pattern[i+1:]]
                return self.match(s[i+1:],pattern[i+1:])
            # 若当前不匹配,判断pattern下一个是否为'*'
            elif pattern[i+1] == '*':
                return self.match(s[i:],pattern[i+2:])
            else:
                return False
        #return True

ss = 'a'
pp = '.'
s = Solution()
print(s.match(ss, pp))