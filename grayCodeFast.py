import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def grayCode(self, n):
		if n == 0:
			return [0]
		result = [0,1]
		for x in range(1, n):
			result = self.duplicate(result, x)
		return result
	def duplicate(self, result, n):
		mask = 1<<n
		length = len(result)
		totalLen = 2*length
		for x in range(length, 2*length):
			result.append(result[totalLen-1-x] | mask)
		return result
		
		 

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		print s.grayCode(10)
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
