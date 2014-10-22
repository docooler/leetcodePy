# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def levelOrderBottom(self, root):
        self.valMap ={}
        if root == None:
            return []
        deep = self.treeDeepVisitor(root,0)
        result = []
        while deep >= 0:
            print "deep :" + str(deep)
            values = self.valMap[deep]
            result.append(values)
            deep -= 1
        return result

    def treeDeepVisitor(self, root, deepLevel):
        if root == None:
            return deepLevel-1
        if self.valMap.has_key(deepLevel):
            values = self.valMap[deepLevel]
            values.append(root.val)
            self.valMap[deepLevel] = values
        else:
            self.valMap[deepLevel] = [root.val]

        deepLeft = self.treeDeepVisitor(root.left, deepLevel+1)
        deepRight = self.treeDeepVisitor(root.right, deepLevel+1)
        if deepLeft > deepRight:
            return deepLeft
        return deepRight


class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
        self.left = None
        self.right = None
        
        
class SolutionUnitTest(unittest.TestCase):
    """docstring for SolutionUnitTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testsingleNumber(self):
        s = Solution()
        print s.levelOrderBottom(None)

    def testCase1(self):
        s = Solution()
        tree = TreeNode(1)
        print s.levelOrderBottom(tree)
    def testCase2(self):
        s = Solution()
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        # tree.right = TreeNode(3)
        print s.levelOrderBottom(tree)

if __name__ == '__main__':
    unittest.main()

