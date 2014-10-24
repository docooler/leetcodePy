import unittest

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def isBalanced(self, root):
        self.minDeep = None

        if root == None:
            return True
        left = True
        right = True
        leftDeep = 0
        rightDeep = 0

        if root.left != None:
           left  =  self.treeDeepVisit(root.left, 0)
           leftDeep = self.minDeep
        if root.right != None:
           right = self.treeDeepVisit(root.right,0)
           rightDeep = self.minDeep
           
        if rightDeep - leftDeep not in [-1, 0, 1]:
            return False
        

        if self.minDeep == None:
            return True
        if left and right:
            return True
        return False

    def treeDeepVisit(self, root, parentDeep):
        selfDeep = parentDeep + 1
        if root.left == None and root.right == None:
            if self.minDeep != None:
                distance = self.minDeep - selfDeep
                if distance > 1 or distance < -1:
                    return False
            else:
                self.minDeep = selfDeep
            return True
        left = True
        right = True
        if root.left != None:
           left =  self.treeDeepVisit(root.left, selfDeep)
        if root.right != None:
           right = self.treeDeepVisit(root.right, selfDeep)
        if left and right:
            return True
        return False
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

    def testCase1(self):
        s = Solution()
        tree = TreeNode(1)
        print s.isBalanced(tree)
    def testCase2(self):
        s = Solution()
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        # tree.right = TreeNode(3)
        print s.isBalanced(tree)

if __name__ == '__main__':
    unittest.main()


        
