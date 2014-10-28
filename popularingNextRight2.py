# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        quene = []
        if root == None:
            return 
        quene.append((0,root))
        fatherDeep = -1
        leftNode = None
        while quene != [] :
            currentDeep, node = quene.pop(0)
            if node.left != None:
                quene.append((currentDeep+1, node.left))
            if node.right != None:
                quene.append((currentDeep+1, node.right))
            if currentDeep != fatherDeep:
                fatherDeep = currentDeep
            else:
                leftNode.next = node
            leftNode = node
