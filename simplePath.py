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
				index += 1
			else:
				if subPath in ['..','.','../', './', ""]:
					if subPath in ['..', '../']:
						try:
							pathStack.pop()
						except Exception, e:
							pathStack = []
						print "back to /"
					subPath = ""
					index += 1
					continue
				else:
					pathStack.append(subPath)
					print "push subPath " + subPath
				subPath = ""

				while index<length and  path[index] == decollator :
					index += 1

		self.pathStack = pathStack

		if len(subPath)>0:
			# print "tail subPath : "+ subPath
			if subPath in ['..','../']:
				try:
					self.pathStack.pop()
				except Exception, e:
					return '/'
			if subPath not in ['..','.','../', './']:
				try:
					lastPath = self.pathStack.pop()
				except Exception, e:
					return self.getPath(subPath)
			
				lastPath = lastPath + '/' + subPath
				self.pathStack.append(lastPath)
		

		retPath = ""
		while len(self.pathStack)>0:
			result = self.pathStack.pop()
			# print result
			sPath = self.getPath(result)
			if sPath == '/':
				continue
			retPath = sPath + retPath
		if retPath == "":
			return '/'
		return retPath

	def getPath(self, result):	
		if result in ["/..", '/.','//'] :
			return '/'
		if result in ['..','../']:
			try:
				self.pathStack.pop()
			except Exception, e:
				return '/'

		if result[0] != '/':
		    result = '/'+ result

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
