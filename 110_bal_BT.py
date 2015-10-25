# Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined 
# as a binary tree in which the depth of the two subtrees of e
# very node never differ by more than 1.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    
    def getHeight(self, root):
        if root == None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
    def isBalanced(self, root):
        if root == None:
            return True
        elif abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False