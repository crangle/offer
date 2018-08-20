# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        que = []
        que.append(pRoot.val)
        next_level = 0
        to_prints = 1
        while not que:
            #print(que[0].val)
            if que[0].left:
                que.append(que[0].left)
                next_level += 1
            if que[0].right:
                que.append(que[0].right)
                next_level += 1
            que.pop(0)
            to_prints -= 1
            if to_prints == 0:
                print('\n')
                to_prints = next_level
                next_level = 0

                