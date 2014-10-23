import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def isValid(self, s):
		symbolStack = []
		symbolMap = {}
		symbolMap['['] = ']'
		symbolMap['('] = ')'
		symbolMap['{'] = '}' 
		index = 0
		while index < len(s):
			sym = s[index]
			index += 1
			if symbolMap.has_key(sym):
				symbolStack.append(sym)
				continue
			
			try:
				topSym = symbolStack.pop()
			except Exception, e:
				return False
			if symbolMap[topSym] != sym:
				return False

		if len(symbolStack) == 0:
			return True
		return False
		
class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testCase1(self):
		# data = [0,1,3,2]
		print "TestCase1"
		s = Solution()
		self.assertEqual(s.isValid("([])"),True)
		self.assertEqual(s.isValid("([{()}])"), True)
		self.assertEqual(s.isValid("([)"), False)
		self.assertEqual(s.isValid("]()"), False)
		# print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")

if __name__ == '__main__':
	unittest.main()
