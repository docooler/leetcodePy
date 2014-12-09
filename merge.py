import unittest

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        j = m
        for x in xrange(n):
            A[j] = B[x]
            j += 1
        A.sort()

class SolutionTest(unittest.TestCase):
    """docstring for SolutionTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
    	s = Solution()
    	s.merge([1],1,[],0)
        out = s.merge([1,2,3,0,0,0],3,[2,5,6],3)
        out = s.merge([],0,[1],1)
        for x in out:
            print x


if __name__ == '__main__':
	unittest.main()
