'''
若二叉树有指向父节点的指针
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    
    def findParent(self, p1, p2, root):
        if p1 == None or p2 == None or root == None:
            return []
        temp = p1
        len1 = 2
        while temp.parent != root:
            temp = temp.parent
            len1 +=1
        temp = p2
        len2 = 2
        while temp.parent != root:
            temp = temp.parent
            len2 += 1
        temp1 = p1
        temp2 = p2
        if len1 > len2:
            for i in range(len1-len2):
                temp1 = temp1.parent
            while temp1.parent != temp2.parent:
                temp1 = temp1.parent
                temp2 = temp2.parent
            return temp1.parent
        else:
            for i in range(len2-len1):
                temp2 = temp2.parent
            while temp1.parent != temp2.parent:
                temp1 = temp1.parent
                temp2 = temp2.parent
                return temp1.parent.val
pN1 = TreeNode(1)
pN2 = TreeNode(2)
pN3 = TreeNode(3)
pN4 = TreeNode(4)
pN5 = TreeNode(5)
pN6 = TreeNode(6)

pN1.left = pN2
pN1.right = pN3
pN2.left = pN4
pN2.right = pN5
pN2.parent = pN1
pN3.parent = pN1
pN4.parent = pN2
pN5.left = pN6
pN5.parent = pN2
pN6.parent = pN5

s = Solution()
print(s.findParent(pN4, pN6, pN1))