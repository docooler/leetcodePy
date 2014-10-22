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
    def isValidBST(self, root):
        if root == None:
            return True
        l = self.inorderTraversal(root)
        for x in xrange(0,len(l)-1):
            if l[x]>=l[x+1]:
                return False
        return True
                
    def inorderTraversal(self, root):
        l = []
        if root == None:
            return l
        if root.left != None:
            left = self.inorderTraversal(root.left)
            l.extend(left)
        l.append(root.val)
        if root.right != None:
            right = self.inorderTraversal(root.right)
            l.extend(right)
        return l    


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
        print "start testsingleNumber"
        s = Solution()
        print s.isValidBST(None)

    def testCase1(self):
        print "start testCase1"
        s = Solution()
        tree = TreeNode(1)
        print s.isValidBST(tree)
    def testCase2(self):
        print "start testCase2"
        s = Solution()
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        print s.isValidBST(tree)

if __name__ == '__main__':
    unittest.main()

