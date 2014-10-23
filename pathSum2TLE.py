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
    def pathSum(self, root, sum):
        self.pathMap = {}
        self.sumSet  = {}
        if root == None:
            return []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        if root.left != None:
            self.visitLeaf(root.left,[root.val], root.val)
        if root.right != None:
            self.visitLeaf(root.right,[root.val], root.val)
        if sum in self.sumSet:
            return self.pathMap[sum] 
        return []
    def visitLeaf(self, root, lPath,fatherSum):
        currSum = fatherSum + root.val
        lPath.append(root.val)
        if root.left == None and root.right == None:
            l =[]
            if currSum in self.sumSet:
                l = self.pathMap[currSum]
            else:
                self.sumSet.add(currSum)

            l.append(lPath)
            self.pathMap[currSum] = l
            return
        if root.left != None:
            self.visitLeaf(root.left,lPath, currSum)
        if root.right != None:
            self.visitLeaf(root.right,lPath, currSum)
        
