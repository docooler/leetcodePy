# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = None
        if preorder == []:
            return root
        self.inorder = inorder
        self.preorder = preorder
        root = TreeNode(0)
        self.build(0, len(inorder), 0 , len(preorder), root)
        return root
        
    def build(self, inStart, inEnd, preStart, preEnd, root):
        val = self.preorder[preStart]
        root.val = val
        
        for x in xrange(inStart, inEnd):
            if val == self.inorder[x]:
                break
        if x != inStart:
            root.left  = TreeNode(0)
            self.build(inStart, x, preStart+1, preStart + (x-inStart)+1, root.left)
        else:
            root.left = None
        if x != inEnd-1:
            root.right = TreeNode(0)
            self.build(x+1, inEnd, preEnd-(inEnd-x)+1, preEnd, root.right)
        else:
            root.right = None
