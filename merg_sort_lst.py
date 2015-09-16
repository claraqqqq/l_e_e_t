# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummyNode = ListNode(0)
        curNode = dummyNode
        while l1 and l2:
            if l1.val < l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        if l1:
            curNode.next = l1
        else:
            curNode.next = l2
        return dummyNode.next
