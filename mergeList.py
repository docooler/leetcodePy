# Definition for singly-linked list.

# https://oj.leetcode.com/problems/merge-two-sorted-lists/

import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printNode(self):
    	print self.val
    	tmp = self.next
    	while tmp != None:
    		print tmp.val
    		tmp = tmp.next


class CreateList(object):
	"""docstring for createList"""
	def create(self, l):
		head = None
		nNode = None
		for x in l:
			temp = ListNode(x)
			nNode = head
			head = temp
			head.next = nNode
		return head



		
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
    	if l1 == None:
    		return l2
    	head = l1
        while l2 != None:
        	tWork = l2
        	l2 = l2.next
        	head = self.__insertNode(head, tWork)
        return head
    def __insertNode(self, l1, l2):
    	if l2.val < l1.val:
    		l2.next = l1
    		return l2
    	head = l1
    	prev = l1
    	while l1 != None:
    		if l2.val < l1.val:
    			break
    		prev = l1
    		l1 = l1.next
    	prev.next = l2
    	l2.next = l1
    	return head
class SolutionTest(unittest.TestCase):
	"""docstring for SolutionTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		c = CreateList()
		l1 = c.create([3,2,1])
		l1.printNode()
		print "============="
		l2 = c.create([5])

		s = Solution()
		l = s.mergeTwoLists(l2,l1)

		l.printNode()
if __name__ == '__main__':
	unittest.main()

		
    	

    	
        	