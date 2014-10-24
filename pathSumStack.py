# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def pathSum(self, root, sum):
        pathMap = {}
        if root == None:
            return []
        stack = [(root,[root.val])]
        while len(stack):
            node,path = stack.pop()
            path.append(node.val)

            if node.left == None and node.right == None:
                lSum = 0
                for x in path:
                    lSum += x
                if pathMap.has_key(lSum):
                    pathMap[lSum].append(path)
                else:
                    pathMap[lSum] = [path]
                continue
                    
            if node.left != None:
                stack.append((node.left, path))
            if node.right != None:
                stack.append((node.right, path))
        if pathMap.has_key(sum):
            return pathMap[sum]
        return []
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
    s = Solution()
    print s.pathSum(head, sum)  
        
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

