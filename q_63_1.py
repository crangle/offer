# -*- coding:utf-8 -*-
# 二叉搜索树的第k个节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = self.inOrder(pRoot)
        return res[k-1]
    def inOrder(self, pRoot):
        lst = []
        def ord(pRoot):
            if pRoot:
                ord(pRoot.left)
                lst.append(pRoot.val)                
                ord(pRoot.right)
        ord(pRoot)
        return lst

pNode1 = TreeNode(5)
pNode2 = TreeNode(3)
pNode3 = TreeNode(7)
pNode4 = TreeNode(2)
pNode5 = TreeNode(4)
pNode6 = TreeNode(6)
pNode7 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.KthNode(pNode1, 3))