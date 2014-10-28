# Definition for a  binary tree node


import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    def printVal(self):
        print self.val
        node = self.left
        while node != None:
            pNode = node
            while pNode != None:
                print pNode.val
                pNode = pNode.next
            node = node.left


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def connect(self, root):
        self.dataMap = {}
        if root == None:
        	return 

        deep = self.treeDeepVisit(root, 0)
        for x in range(deep+1):
            lNode = self.dataMap[x]
            nCnt = len(lNode)
            # print "x: " + str(x) +" nCnt : " + str(nCnt)
            for i in range(nCnt-1):
                # print "i : " + str(i)
                lNode[i].next = lNode[i+1]
            lNode[nCnt-1].next = None
        return

    def treeDeepVisit(self, root, deepLevel):
    	if root == None:
    		return deepLevel -1

    	nodes = []
    	if deepLevel in self.dataMap:
    		nodes = self.dataMap[deepLevel]
    	nodes.append(root)
    	self.dataMap[deepLevel] = nodes

    	
    	leftDeep  = self.treeDeepVisit(root.left,  deepLevel+1)
        rightDeep = self.treeDeepVisit(root.right, deepLevel+1)
    	if rightDeep > leftDeep:
    		return rightDeep
    	return leftDeep

class Solution_Test(unittest.TestCase):
    """docstring for Solution"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
        print "start testCase1"
        t = TreeNode(1)
        s = Solution()
        s.connect(t)
        t.printVal()
    def testCase2(self):
        print "start testCase2"
        t = TreeNode(1)
        t.left = TreeNode(2)
        t.right = TreeNode(3)
        s = Solution()
        s.connect(t)
        t.printVal()
if __name__ == '__main__':
    unittest.main()

    		


        
        
