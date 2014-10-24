# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest

class Solution:
    def pathSum(self, root, sum):
        paths = []
        if root == None:
            return []
        stack = [(root,[root.val], sum)]
        while not stack == []:
            node, path, lSum = stack.pop()
            path.append(node.val)

            if node.left == None and node.right == None:
                if lSum == node.val:
                    paths.append(path)
                continue
                    
            if node.left != None:
                stack.append((node.left, path, lSum-node.val))
            if node.right != None:
                stack.append((node.right, path, lSum-node.val))
        # print "len of path :" + str(len(paths)) 
        return paths

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
        self.left = None
        self.right = None
def MutileTree():
    tree = TreeNode(0)
    head = tree
    sum = 0
    for x in xrange(1,1000):
        tree.right = TreeNode(x)
        tree = tree.right
        sum += x
    
    i = 999
    tree = head
    while i > 0:
        tree.left = TreeNode(i)
        tree = tree.left
        i -= 1


    s = Solution()
    s.pathSum(head, sum)  
        
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
    # unittest.main()
    MutileTree()

