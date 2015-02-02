# Remove Nth Node From End of List
# Given a linked list, remove the nth node from 
# the end of list and return its head.
# For example,
#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, 
# the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        node1 = head
        node2 = head
        node2prev = None
        while n > 0:
            node1 = node1.next
            n -= 1
        while node1 != None:
            node2prev = node2
            node1 = node1.next
            node2 = node2.next
        if node2prev == None:
            return head.next
        node2prev.next = node2prev.next.next
        return head