# Definition for singly-linked list with a random pointer.

import unittest

class  SolutionTest(unittest.TestCase):
    """docstring for  SolutionTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
        rList = RandomListNode(1)
        rList.random = RandomListNode(2)

        s= Solution()
        s.copyRandomList(rList)
    def  testCase2(self):
        s = Solution()
        r = s.copyRandomList(None)
        self.assertEqual(r, None)

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def __init__(self):
        self.nodeMap = {}
    def copyRandomList(self, head):
        nodeMap = self.nodeMap
        randomList = []
        if head == None:
            return None
            
        temp = head
        nHead = None
        nPrev = None
        while temp != None:
            node = RandomListNode(temp.label)
            if nodeMap.has_key(temp) == False:
                nodeMap[temp] = node
            else:
                break
            if temp.random != None:
                if nodeMap.has_key(temp.random) == False:
                    randomList.append((node,temp))
                else:
                    node.random = nodeMap[temp.random]
            
            if nHead == None:
                nHead = node
                nPrev = node
            else:
                nPrev.next = node
                nPrev = nPrev.next
            temp = temp.next
        while randomList != []:
            node, srcNode = randomList.pop()
            if nodeMap.has_key(srcNode.random) == False:
                node.random = self.copyRandomList(srcNode.random)
            else:
                node.random = nodeMap[srcNode.random]
        return nHead
        
if __name__ == '__main__':
    unittest.main()

        
        
                
            
            
        