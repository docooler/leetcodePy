# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
                def rob(self, root):
                                """
                                :type root: TreeNode
                                :rtype: int
                                """
                                if root == None:
                                                return 0

                                v1, v2  = self.findMax(root)
                               

                                return max(v1, v2)

                def findMax(self, root):
                                if root == None:
                                                return 0, 0

                                maxWithRoot    = 0
                                maxWithOutRoot = 0

                                if root.left != None and root.right != None:
                                                l1, l2 = self.findMax(root.left)
                                                r1, r2 = self.findMax(root.right)
                                                maxWithRoot = root.val + l2 + r2
                                                maxWithOutRoot = max(l1, l2) + max(r1, r2)
                                elif root.left == None and root.right == None:
                                                maxWithRoot    = root.val
                                                maxWithOutRoot = 0
                                elif root.left == None:
                                                r1, r2 = self.findMax(root.right)
                                                maxWithRoot = root.val + r2
                                                maxWithOutRoot = max(r1, r2)
                                else:
                                                l1, l2 = self.findMax(root.left)
                                                maxWithRoot = root.val + l2
                                                maxWithOutRoot = max(l1, l2)

                                return maxWithRoot, maxWithOutRoot
