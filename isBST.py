import unittest

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def isBalanced(self, root):
        if root == None:
            return True
        lDeep = self.getNodeDepth(root.right)
        rDeep = self.getNodeDepth(root.left)
        return (abs(lDeep - rDeep) < 2 and self.isBalanced(root.right) and self.isBalanced(root.left))


        
    def getNodeDepth(self, node):
        if(node==None):return 0;

        stack=[(node,1)];
        dep=1;

        while(len(stack)):
            first,dep=stack.pop(0)
            if(first.left!=None):
                stack.append((first.left,dep+1))
            if(first.right!=None):
                stack.append((first.right,dep+1))
        return dep

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


        
