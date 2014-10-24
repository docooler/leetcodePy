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
    def flatten(self, root):
        lNodeStack = []
        if root == None:
            return root
        
        if root.right != None:
            lNodeStack.append(root.right)
            root.right = None
        if root.left != None:
            lNodeStack.append(root.left)
            root.left = None
        pTree = root
        while len(lNodeStack)>0:
            node = lNodeStack.pop()
            if node.right != None:
                lNodeStack.append(node.right)
                node.right = None
            if node.left != None:
                lNodeStack.append(node.left)
                node.left  = None
            pTree.right = node
            pTree = pTree.right
        return root





class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
        self.left = None
        self.right = None
    def printRight(self):
        print str(self.val)
        tNode = self.right
        while tNode != None:
            print str(tNode.val)
            tNode = tNode.right
        
        
class SolutionUnitTest(unittest.TestCase):
    """docstring for SolutionUnitTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass

    def testCase1(self):
        print "testCase1"
        s = Solution()
        tree = TreeNode(1)
        s.flatten(tree).printRight()
    def testCase2(self):
        print "testCase2"
        s = Solution()
        tree = TreeNode(1)
        tree.right = TreeNode(2)
        # tree.right = TreeNode(3)
        s.flatten(tree).printRight()
    def  testCase3(self):
        print "testCase3"
        s = Solution()
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        # tree.right = TreeNode(3)
        s.flatten(tree).printRight()


if __name__ == '__main__':
    unittest.main()

