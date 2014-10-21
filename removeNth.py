import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def removeNthFromEnd(self, head,n):
		nCnt = 1
		node = head
		while node.next != None:
			nCnt += 1
			node = node.next
			# print node.val
		node = head
		prev = head
		# print "removed node is :" + str(nCnt-n)
		if nCnt == n:
			return head.next

		for x in range(nCnt-n):
			prev = node
			node = node.next
			# print str(node.val)
		prev.next = node.next
		return head

class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		super(ListNode, self).__init__()
		self.val = x
		self.next = None
		

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		head = ListNode(1)
		node2= ListNode(2)
		head.next = node2
		node3 = ListNode(3)
		node2.next = node3
		node4 = ListNode(4)
		node3.next = node4
		node5 = ListNode(5)
		node4.next = node5
        
		head = s.removeNthFromEnd(head,2)
		while head.next != None:
			print head.val
			head = head.next
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
