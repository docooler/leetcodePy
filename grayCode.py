import unittest

class Solution:
	# @param A, a list of integer
    # @return an integer
	def grayCode(self, n):
		self.used = []
		self.len  = n
		self.data = []

		# print "data len " + str(self.len)
		current = 0
		self.data.append(current)
		self.used.append(current)
		# print "data length is " + str(len(self.data))
		# print "all data num is " + str(1<<self.len)
		while len(self.data) < (1<<self.len):		
			current = self.getNext(current)
			# if current == None:
			# 	break
			self.used.append(current)
			self.data.append(current)
		# print self.data
		return self.data
	def getNext(self, current):
		# print "enter getNext"
		for x in xrange(0,self.len):
			data = self.changeOneBit(current, x, 1)
			# print "changeOneBit 1 return :" + str(data)
			if data not in self.used:
				return data

			data = self.changeOneBit(current, x, 0)
			# print "changeOneBit 1 return :" + str(data)
			if data not in self.used:
				return data

	def changeOneBit(self, current, offset, setbit):
		if setbit:
			mask = 1<<offset
			return current | mask
		else:
			mask = ~(1<<offset)
			return  current & mask

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		for x in xrange(0,7):
			print str(x) + "is :"
			print s.grayCode(x)
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()