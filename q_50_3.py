'''
普通树寻找第一个共同祖先节点
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        #self.parent = None
class Solution:
    
    def lowestComAnc(self, p1, p2, root):
        path1 = self.findPath(p1, root)
        path2 = self.findPath(p2, root)
        for i in range(len(path1)):
            if path1[i] != path2[i]:
                return path1[i-1]
    

    def findPath(self, p, root):
        if root == None or p == None:
            return []
        elif root.val == p.val:
            return [[p]]
        path = []
        if root.left:
            stackleft = self.findPath(root.left, p)
            if stackleft:
                path.append(stackleft[0].insert(0, root))
        if root.right:
            stackright = self.findPath(root.right, p)
            if stackright:
                path.append(stackright[0].insert(0, root))
        return path

# 二叉树的最低公共祖先
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == None:
            return False
        pathA = self.storeNodes(root, A)[0]
        pathB = self.storeNodes(root, B)[0]
        if pathA and pathB:
            lenA, lenB = len(pathA), len(pathB)
            diff = abs(lenA - lenB)
            if lenA > lenB:
                markA = lenA - diff - 1
                markB = lenB - 1
            else:
                markA = lenA - 1
                markB = lenB - diff - 1
            while markA >= 0 and markB >= 0:
                if pathA[markA] == pathB[markB]:
                    return pathA[markA]
                markA -= 1
                markB -= 1

    def storeNodes(self, root, targetNode):
        if root == None or targetNode == None:
            return []
        elif root.val == targetNode.val:
            return [[targetNode]]
        stack = []
        if root.left:
            stackLeft = self.storeNodes(root.left, targetNode)
            for i in stackLeft:
                i.insert(0, root)
                stack.append(i)
        if root.right:
            stackRight = self.storeNodes(root.right, targetNode)
            for i in stackRight:
                i.insert(0, root)
                stack.append(i)
        return stack