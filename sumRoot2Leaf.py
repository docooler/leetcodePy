# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.sum = 0
        if root == None:
            return 0
        if (root.left == None) and (root.right == None):
            return root.val
        if root.left != None:
            self.visitLeaf(root.left, root.val)
        if root.right != None:
            self.visitLeaf(root.right, root.val)
        return self.sum
    def visitLeaf(self, root, fatherNum):
        num = fatherNum * 10 + root.val
        if (root.left==None) and (root.right==None):
            self.sum += num
            return 
        if root.left != None:
            self.visitLeaf(root.left, num)
        if root.right != None:
            self.visitLeaf(root.right, num)
        return 
        
        
        
