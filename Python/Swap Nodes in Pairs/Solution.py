# Problem: Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Note: Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#
################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        fast, slow, move = head.next, head, None

        while slow.next:
            slow.next = fast.next
            fast.next = slow
            if move:
                move.next = fast
            else:
                head = fast
            move = slow

            if slow.next and slow.next.next:
                fast = slow.next.next
                slow = slow.next
            else:
                break

        return head
