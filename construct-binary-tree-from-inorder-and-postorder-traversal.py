# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
       
        root = None
        if postorder == []:
            return None
        self.inorder = inorder
        self.postorder = postorder
        root = TreeNode(0)
        self.build(0,len(inorder), 0, len(postorder), root)
        return root
    def build(self, inStart, inEnd, postStart, postEnd, root):
        val = self.postorder[postEnd-1]
        root.val = val
        
        for x in xrange(inStart, inEnd):
            if val == self.inorder[x]:
                break
        if x != inStart:
            root.left  = TreeNode(0)
            self.build(inStart, x, postStart, postStart + (x-inStart), root.left)
        else:
            root.left = None
        if x != inEnd-1:
            root.right = TreeNode(0)
            self.build(x+1, inEnd, postEnd-(inEnd-x), postEnd-1, root.right)
        else:
            root.right = None
