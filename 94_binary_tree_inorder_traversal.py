# Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its 
# nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it 
# iteratively?
# Tree traversal: http://en.wikipedia.org/wiki/Tree_traversal
# Depth-first
# There are three types of depth-first traversal: pre-order, in
# -order, and post-order. For a binary tree, they are defined 
# as display operations recursively at each node, starting 
# with the root node, whose algorithm is as follows:

# Pre-order
# 
# Display the data part of root element (or current element)
# Traverse the left subtree by recursively calling the pre-
# order function.
# Traverse the right subtree by recursively calling the pre-
# order function.

# In-order (symmetric)
# 
# Traverse the left subtree by recursively calling the in-
# order function.
# Display the data part of root element (or current element).
# Traverse the right subtree by recursively calling the in-
# order function.

# Post-order
# 
# Traverse the left subtree by recursively calling the post-
# order function.
# Traverse the right subtree by recursively calling the post-
# order function.
# Display the data part of root element (or current element).


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                parent = stack.pop()
                result.append(parent.val)
                cur = parent.right
        return result
