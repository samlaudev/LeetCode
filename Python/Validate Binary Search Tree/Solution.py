# Problem: Validate Binary Search Tree
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#  1. The left subtree of a node contains only nodes with keys less than the node's key.
#  2. The right subtree of a node contains only nodes with keys greater than the node's key.
#  3. Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#     2
#   / \
#  1   3
#
# Binary tree [2,1,3], return true.
#
# Example 2:
#     1
#   / \
#  2   3
#
# Binary tree [1,2,3], return false.
#
################################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTRecursive(root, float('-inf'), float('inf'))

    def isValidBSTRecursive(self, root, low, high):
        if not root:
            return True

        return low < root.val and root.val < high and \
            self.isValidBSTRecursive(root.left, low, root.val) and \
            self.isValidBSTRecursive(root.right, root.val, high)
