import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def candy(self, ratings):
		self.len     = len(ratings)
		self.handle  = 0
		self.marked  = [ 0 for i in range(self.len)]
		self.candies = [1 for i in range(self.len)]
		if self.len == 1:
			return 1

		while self.handle < self.len:
			index = self.getLowestRate(ratings)
			self.localGreedy(index,ratings)
			self.marked[index] = 1
			self.handle += 1
		allCandy = 0
		for num in self.candies:
			allCandy += num
		return allCandy
	def localGreedy(self, index, ratings):
		i = index
		while i > 0:
			# print "left i :" + str(i)
			if ratings[i] < ratings[i-1]:
				if self.candies[i] >= self.candies[i-1]:
					self.candies[i-1] = self.candies[i] + 1
					i -= 1
				else:
					break
			else:
				break
		i = index
		while i<self.len-1:
			if ratings[i] < ratings[i+1]:
				if self.candies[i] >= self.candies[i+1]:
					self.candies[i+1] = self.candies[i] + 1
					i += 1
				else:
					break
			else:
				break

	def getLowestRate(self,ratings):
		lowest = None
		index  = None
		for x in xrange(self.len):
			if self.marked[x] != 1:
				if lowest == None:
					lowest = ratings[x]
					index = x
				if lowest > ratings[x]:
					lowest = ratings[x]
					index = x

		return index
class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		print s.candy([1,2,1,3])
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
