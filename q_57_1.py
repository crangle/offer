# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead.next:
            temp = pHead
            while pHead == temp.next:
                temp = temp.next
            pHead = temp.next
            # temp = pHead.next
            pHead.next = self.deleteDuplication(pHead)
            return pHead
        else:
            return pHead

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# node6.next = node3

s = Solution()
print(s.deleteDuplication(node1).val)