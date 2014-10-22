# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        l = []
        if root == None:
            return l

        l.append(root.val)
        
        if root.left != None:
            left = self.preorderTraversal(root.left)
            l.extend(left)
        if root.right != None:
            right = self.preorderTraversal(root.right)
            l.extend(right)

        return l
        