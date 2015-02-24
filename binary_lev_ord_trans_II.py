# Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal 
# of its nodes' values. (ie, from left to right, level by level 
# from leaf to root).
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        result = []
        curNodes = [root]
        while curNodes:
            nextNodes = []
            curNodesVals = []
            for node in curNodes:
                curNodesVals.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            curNodes = nextNodes
            result.insert(0, curNodesVals)
        return result