# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 先找环中节点数目
        # 再进行先后指针往前走
        if pHead.next == None or pHead.next.next == None:
            return "null"
        p1 = pHead
        p2 = pHead
        while p1.next.next != p2.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1.next.next == None:
                return "null"
        p3 = p1
        iLoop = 1
        while p1.next != p3:
            p1 = p1.next
            iLoop += 1
        p1 = pHead
        p2 = pHead
        for i in iLoop:
            p2 = p2.next
        while p1.next != p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)