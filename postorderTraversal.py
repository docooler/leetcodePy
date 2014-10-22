# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        l = []
        if root == None:
            return l
        
        if root.left != None:
            left = self.postorderTraversal(root.left)
            l.extend(left)
        if root.right != None:
            right = self.postorderTraversal(root.right)
            l.extend(right)
        l.append(root.val)
        return l
        