# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.viewList = []
        self.viewTree(root,0)
        return self.viewList
    def viewTree(self, root, deep):
        if root == None:
            return
        if deep >= len(self.viewList):
            self.viewList.append(root.val)
        else:
            self.viewList[deep] = root.val
        self.viewTree(root.left, deep+1)
        self.viewTree(root.right,deep+1)
