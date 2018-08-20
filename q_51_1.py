# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        i = 0
        while i < len(numbers):
            if i == numbers[i]:
                i += 1
                continue
            elif numbers[i] == numbers[numbers[i]]:
                duplication[0] = numbers[i]
                return True
            else:
                numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
        return False

s = Solution()
n = [2,3,1,0,2,5,3]
d = []
print(s.duplicate(n,d))


if numbers == None or len(numbers) <= 0:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return False