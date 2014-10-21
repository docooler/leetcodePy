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
        l = []
        if root == None:
            return l
        if root.left != None:
            left = self.inorderTraversal(root.left)
            l.extend(left)
        l.append(root.val)
        if root.right != None:
            right = self.inorderTraversal(root.right)
            l.extend(right)
        return l
        