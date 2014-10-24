import unittest


# f(0) = [0]
# f(1) = [0,1]
# f(n+1) = duplicate(f(n)) 


class Solution:
	# @param A, a list of integer
    # @return an integer
	def simplifyPath(self, path):
		absPath = []
		subPaths = path.split('/')
		length = len(subPaths)

		for sPath in subPaths:
			if sPath == '..':
				if not absPath == []:
					absPath.pop()
			
			if sPath not in ['.', '..', '']:
				absPath.append(sPath)
		if len(absPath) == 0:
			return '/'
		result = ""
		for p in absPath:
			result = result + '/' + p
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
		self.assertEqual(s.simplifyPath("/path/haha/"),"/path/haha")
		self.assertEqual(s.simplifyPath("/path//haha/"), '/path/haha')
		self.assertEqual(s.simplifyPath("/path////haha/"), '/path/haha')
		self.assertEqual(s.simplifyPath("/path////haha/../../../"), '/')
		self.assertEqual(s.simplifyPath("/"),'/')
		self.assertEqual(s.simplifyPath("/..."),'/...')
		self.assertEqual(s.simplifyPath("/home/abc"), '/home/abc')
		self.assertEqual(s.simplifyPath("/home"),'/home')
		self.assertEqual(s.simplifyPath("///"), '/')
		self.assertEqual(s.simplifyPath("/home/../../.."), '/')
		self.assertEqual(s.simplifyPath("/home/foo/"), '/home/foo')
		self.assertEqual(s.simplifyPath("/a/./b/../../c/"),'/c')
		self.assertEqual(s.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/"), '/home/foo/.ssh2/authorized_keys')
		self.assertEqual(s.simplifyPath("/hzx/.././BVHm/../././..//"), '/')
		self.assertEqual(s.simplifyPath("///eHx/.."), '/')
		self.assertEqual(s.simplifyPath("/home/foo/./bar/"), "/home/foo/bar")
		self.assertEqual(s.simplifyPath("/home/foo/./....bar/"), "/home/foo/....bar")
		self.assertEqual(s.simplifyPath("/home/of/foo/."), '/home/of/foo')
		self.assertEqual(s.simplifyPath("/home/of/foo/./"), '/home/of/foo')
		self.assertEqual(s.simplifyPath("/home/of/foo/abc/./..//////"), '/home/of/foo')
		self.assertEqual(s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"), "/e/f/g")
		# # self.assertEqual(s.simplifyPath("]()"), False)
		# # print str(len(r_data))
        # print r_data
		# self.assertEqual(r_data ,data, "test failed")

if __name__ == '__main__':
	unittest.main()
