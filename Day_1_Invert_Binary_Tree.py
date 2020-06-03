# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:48:33 2020

@author: vivek
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        rightInverted = self.invertTree(root.right)
        leftInverted = self.invertTree(root.left)
        root.left = rightInverted
        root.right = leftInverted
        return root