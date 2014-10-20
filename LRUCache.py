import random
import unittest

class LRUCache:

    # @param capacity, an integer
	def __init__(self, capacity):
		self.capa = capacity
		self.dic  = {}
		self.allKey = []    
		self.len    = 0
    # @return an integer
	def get(self, key):
		if key in self.allKey:
			self.updateKey2Head(key)
			return self.dic[key]
		else:
			return -1
	def updateKey2Head(self,key):
		self.allKey.remove(key)
		self.allKey.insert(0,key)
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
	def set(self, key, value):
		if self.len == self.capa:
			if key not in self.allKey:
				oldkey = self.allKey.pop()
				self.allKey.append(key)
				self.dic[key] = value
				self.dic[oldkey] = -1
			else:
				self.dic[key] = value
		else:
			if key in self.allKey:
				self.dic[key] = value
			else:
				self.allKey.append(key)
				self.dic[key] = value
			self.len += self.len + 1


class Solution_test:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        datamap = {}
        for i in A:
        	if datamap.has_key(i):
        		datamap[i] = 2
        	else:
        		datamap[i] = 1
        for (key, value) in datamap.items():
        	if value == 1:
        		return key

class SolutionUnitTest(unittest.TestCase):
	"""docstring for SolutionUnitTest"""
	def setup(self):
		pass
	def tearDown(self):
		pass
	def testsingleNumber(self):
		l = LRUCache(10)
		# for x in xrange(1,11):
		# 	l.set(x,x)
		# for x in xrange(1,11):
		# 	print str(x) + "=>" + str(l.get(x))
		# print "\n"
		# for x in xrange(11,20):
		# 	l.set(x,x)
		# 	print str(x) + "=>" + str(l.get(x))
		# 	print str(x-10) + "=>" + str(l.get(x-10))
	def testcase2(self):
		l = LRUCache(2)
		l.set(2,1)
		l.set(1,1)
		l.set(2,3)
		l.set(4,1)
		print l.get(1)
		print l.get(2)
	def testBig(self):
		l = LRUCache(2048)
		
		for x in xrange(1,4096):
			l.set(x, random.randint(1,4096))
			print l.get(x)





if __name__ == '__main__':
	unittest.main()