# Problem: Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 检查为空
        if not l1:
            return l2
        if not l2:
            return l1

        # 生成排序后的list
        list, first, second = [], l1, l2

        while first and second:
            if first.val < second.val:
                list.append(first.val)
                first = first.next
            elif first.val > second.val:
                list.append(second.val)
                second = second.next
            else:
                list.append(first.val)
                list.append(second.val)
                first = first.next
                second = second.next

        while first:
            list.append(first.val)
            first = first.next

        while second:
            list.append(second.val)
            second = second.next

        # 连接l1和l2
        first, second = l1, l2
        while first and second and first.next and second.next:
            first = first.next
            second = second.next

        if first and not first.next:
            first.next = l2

            # 给连接后linked list赋值
            iter = l1
            for val in list:
                iter.val = val
                iter = iter.next

            return l1

        if second and not second.next:
            second.next = l1

            # 给连接后linked list赋值
            iter = l2
            for val in list:
                iter.val = val
                iter = iter.next

            return l2

        return None
