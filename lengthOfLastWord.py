import unittest

class Solution:
	# @param A, a list of integer
    # @return an integer
	def lengthOfLastWord(self, s):
		l = s.split(' ')
		length = len(l)
		index = -1
		empty = 0

		while index >= -length:
			if l[index] == '':
				empty += 1
				index -= 1
			else:
				break
		# print "length : " + str(length)
		# print "empty  : " + str(empty)
		# print "index  : " + str(index)

		if empty == length:
			return 0
		if index < -length:
			return 0
		    
		return len(l[index])
      


class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		# data = [0,1,3,2]
		s = Solution()
		self.assertEqual(s.lengthOfLastWord("a "), 1)
		self.assertEqual(s.lengthOfLastWord('a'),1)
		self.assertEqual(s.lengthOfLastWord("    "), 0)
		self.assertEqual(s.lengthOfLastWord(" "), 0)
		self.assertEqual(s.lengthOfLastWord(""),0)
		# self.assertEqual(s.lengthOfLastWord("b   a     "), 1)
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")



if __name__ == '__main__':
	unittest.main()
	# s = Solution()
	# s.grayCode(10)
