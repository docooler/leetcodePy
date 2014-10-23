# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        self.lSum = []
        if root == None:
            return False
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False
        if root.left != None:
            self.visitLeaf(root.left, root.val)
        if root.right != None:
            self.visitLeaf(root.right, root.val)
        if sum in self.lSum :
            return True
        return False
    def visitLeaf(self, root, fatherNum):
        num = fatherNum + root.val
        if root.left == None and root.right == None:
            self.lSum.append(num)
            return
        if root.left != None:
            self.visitLeaf(root.left, num)
        if root.right != None:
            self.visitLeaf(root.right, num)
        
