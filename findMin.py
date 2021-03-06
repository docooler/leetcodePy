import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def maxProduct(self, num):
		result  = num[0] * num[1]
		index   = 0
		for x in xrange(1,len(num)):
			temp = num[x] * num[x+1]
			if result < temp:
				result = temp
				index = x
		return num[x:x+1]
			

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		print s.maxProduct([4,5,6,7,0,1,2,3])
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
