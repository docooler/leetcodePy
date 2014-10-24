import unittest

class Solution:
	# @param A, a list of integer
    # @return an integer
	def maxProfit(self, prices):
		mProfit = 0
		totalProfit = 0

		length = len(prices)-1
		if length < 0:
			return 0
		bestSellPoint = prices[length]
		while length >= 0:
			temp = bestSellPoint - prices[length]
			if temp > 0 :
				if mProfit < temp:
					mProfit = temp
			else:
				bestSellPoint = prices[length]
				totalProfit += mProfit
				mProfit = 0
			length -= 1
		totalProfit += mProfit

		return totalProfit


class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		self.assertEqual(s.maxProfit([3,2,1]) ,0)
		self.assertEqual(s.maxProfit([1,5,2,15,3,1,7]),6+14)
		self.assertEqual(s.maxProfit([6,1,3,2,4,7]), 7)
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
	# s = Solution()
	# s.grayCode(10)
