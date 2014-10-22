import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def reorderList(self, head):
		nodeMap = {}
		if head == None:
			# print "return head None"
			return head
		index = 0
		node = head
		while node != None:
			nodeMap[index] = node
			node = node.next
			index += 1
		# print "index : " + str(index)
		start = ListNode(0)
		node  = start
		for i in xrange(0,((index+1)/2)):
			# print "i: " + str(i)
			# print "val:" + str(nodeMap[i].val)
			node.next = nodeMap[i]
			node = node.next

			if i == index-i-1:
				node.next = None
				break
			# print "val:" + str(nodeMap[index-i-1].val)
			node.next = nodeMap[index-i-1]
			node = node.next
			node.next = None
		return start.next


class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		super(ListNode, self).__init__()
		self.val = x
		self.next = None
	def printVal(self):
		print self.val
		node = self.next
		while node != None:
			print node.val
			node = node.next
	

class SList(object):
	"""docstring for SList"""
	def __init__(self):
		super(SList, self).__init__()
		self.head = None
	def append(self, inode):
		if self.head == None:
			self.head = inode
		prev = self.head
		node = self.head.next
		while node != None:
			prev = node
			node = node.next
		prev.next = inode
		inode.next = None
	def appendInt(self, key):
		node = ListNode(key)
		self.append(node)

	def printVal(self):
		node = self.head
		while node != None:
			print node.val
			node = node.next


		
		

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		print "start testsingleNumber"
		s = Solution()
		
		head = SList()

		head.append(ListNode(1))
		head.append(ListNode(2))
		head.append(ListNode(3))
		head.append(ListNode(4))

		node = s.reorderList(head.head)
		if node != None:
			node.printVal()
			pass
		else:
			print node
	def testCase1(self):
		print "start testCase1"
		slist = SList()
		slist.append(ListNode(1))
		s = Solution()
		node = s.reorderList(slist.head)
		node.printVal()
	def testCase2(self):
		print "start testCase2"
		slist = SList()
		slist.appendInt(1)
		slist.appendInt(2)
		s = Solution()
		node = s.reorderList(slist.head)
		node.printVal()




if __name__ == '__main__':
	unittest.main()
