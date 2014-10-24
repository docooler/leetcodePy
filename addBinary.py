import unittest

class Solution:
	# @param A, a list of integer
    # @return an integer
	def addBinary(self, m,n):
		mLen = len(m)
		nLen = len(n)

		if mLen > nLen:
			lowLen = nLen
			maxLen = mLen
			longStr = m
		else:
			lowLen = mLen
			maxLen = nLen
			longStr = n

		index = -1
		result = ""
		carrier = 0
		while index >= -lowLen:
			x =  int(m[index]) + int(n[index]) + carrier
			carrier = x/2
			x = x%2
			result = str(x) + result
			index -= 1

		while index >= -maxLen:
			x = int(longStr[index]) + carrier
			carrier = x/2
			x = x%2
			result = str(x) + result
			index -= 1
		if carrier == 1:
			result = '1' + result
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
		self.assertEqual(s.addBinary('1','1'),'10')
		self.assertEqual(s.addBinary('10','11110'),'100000')
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
	# s = Solution()
	# s.grayCode(10)
