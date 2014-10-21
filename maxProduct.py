import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def maxProduct(self, num):
		length = len(num)
		result = 1
		if length == 1:
			return num[0]
		nminasCnt = 0
		for x in num:
			if x < 0:
				nminasCnt ++
		if nminasCnt%2==0:
			for x in num:
				result *= x
			return result
		else:
			result 
				

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
		print s.maxProduct([0,2])
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
