import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 

class Solution:
	# @param A, a list of integer
    # @return an integer
	def simplifyPath(self, path):
		pathStack = []
		decollator = '/'
		index = 1
		subPath = '/'
		length = len(path)
		while index < length:
			l = path[index]
			# print l
			if l != decollator:
				subPath += l
				# print subPath
			else:
				if index+1<length and path[index+1] == decollator:
					subPath += '/'

					while index<length and  path[index] == decollator :
						index += 1
					continue
				
				pathStack.append(subPath)
				print "push subPath " + subPath
				subPath = ""

			index += 1
		try:
			result = pathStack.pop()
		except Exception, e:
			return '/'

		while result == "..":
			result = pathStack.pop()
		if result == "/..":
			return '/'
		return result
		
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
		# result = s.simplifyPath("/path/haha/")
		# print result
		# self.assertEqual(result,'haha')
		self.assertEqual(s.simplifyPath("/path//haha/"), '/path/haha')
		self.assertEqual(s.simplifyPath("/path////haha/"), '/path/haha')
		self.assertEqual(s.simplifyPath("/path////haha/../../../"), '/path/haha')

		# # self.assertEqual(s.simplifyPath("]()"), False)
		# # print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")

if __name__ == '__main__':
	unittest.main()
