import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def deleteDuplicates(self, head):
		valMap = {}
		if head == None:
			return None
		node = head
		while node != None:
			if valMap.has_key(node.val):
				valMap[node.val] += 1
			else:
				valMap[node.val] = 1
			node = node.next
		while head != None:
			if valMap[head.val] > 1:
				head = head.next
			else:
				break
		if head == None:
			return None
		node = head.next
		run  = head
		while node != None:
			if valMap[node.val] == 1:
				run.next = node
				run = run.next
			node = node.next
		run.next = None
		return head
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
		s = Solution()
		
		head = SList()

		head.append(ListNode(1))
		head.append(ListNode(1))
		head.append(ListNode(2))
		head.append(ListNode(2))

		node = s.deleteDuplicates(head.head)
		if node != None:
			node.printVal()
		else:
			print node
		
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
