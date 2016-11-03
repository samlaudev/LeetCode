# Problem: Binary Tree Paths
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
# \
#  5
#
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path, result = [], []
        self.binaryTreePathsRecursive(root, path, result)
        return result

    def binaryTreePathsRecursive(self, node, path, result):
        if not node:
            return

        if not node.left and not node.right:
            path_text = ""
            for val in path:
                path_text += str(val) + "->"
            path_text += str(node.val)
            result.append(path_text)

        if node.left:
            path.append(node.val)
            self.binaryTreePathsRecursive(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node.val)
            self.binaryTreePathsRecursive(node.right, path, result)
            path.pop()
