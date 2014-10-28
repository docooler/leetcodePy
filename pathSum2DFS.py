# Definition for a  binary tree node
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def pathSum(self, root, sum):
        result = []
        stack = []
        if root == None:
            return result
       
        
        stack.append((root, []))

        while stack != []:
            node, l = stack.pop()
            l.append(node.val)

            if node.left == None and node.right == None:
                lSum = 0
                # print l
                for x in l:
                    lSum += x
                # print "lSum : " +  str(lSum)
                if lSum == sum:
                    result.append(l)
            else:
                if node.left != None:
                    stack.append((node.left, l[:]))
                if node.right != None:
                    stack.append((node.right, l[:]))
        return result

class SolutionTest(unittest.TestCase):
    """docstring for SolutionTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
        print "testCase1"
        t = TreeNode(1)
        t.left = TreeNode(2)
        t.right = TreeNode(3)

        s = Solution()
        result = s.pathSum(t, 3)
        self.assertEquals(result,[[1,2]])
        for i in result:
            print i
if __name__ == '__main__':
    unittest.main()
        
               
