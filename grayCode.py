import unittest

class Solution:
	# @param A, a list of integer
    # @return an integer
	def grayCode(self, n):
		self.used = []
		self.num  = n
		self.data = []
		self.dataLen(n)

		print "data len " + str(self.len)
		current = 0
		self.data.append(current)
		self.used.append(current)
		print "data length is " + str(len(self.data))
		while len(self.data) <= n+1:		
			current = self.getNext(current)
			self.used.append(current)
			self.data.append(current)
		print self.data
		return self.data
	def dataLen(self, n):
		self.len = 1
		while 1:
			if n == 0:
				return
			else:
				n = n>>1
				self.len = self.len +  1
	def getNext(self, current):
		print "enter getNext"
		for x in xrange(0,self.len-1):
			data = self.changeOneBit(current, x, 1)
			if data not in self.used:
				if data <= self.num:
					print "getNext return" + str(data)
					return data

			data = self.changeOneBit(current, x, 0)
			if data not in self.used:
				if data <= self.num:										
					print "getNext return" + str(data)
					return data

	def changeOneBit(self, current, offset, zero):
		if zero:
			mask = 1<<offset
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
		data = [0,1,3,2]
		s = Solution()
		r_data = s.grayCode(2)
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()