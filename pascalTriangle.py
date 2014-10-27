import unittest

class Solution:
    # @param s, a string
    # @return a boolean
    def generate(self, numRows):
        tMap = {}
        tMap[1] = [1]
        tMap[2] = [1,1]
        for x in range(3, numRows+1):
            l = [1] * x
            # print x
            for i in xrange(1,x-1):
                l[i] = tMap[x-1][i-1] + tMap[x-1][i]
            tMap[x] = l
        result = [[]] * numRows
        # print "generate result"
        # print tMap[3]
        for x in range(numRows):
            # print x
            result[x] = tMap[x+1]
        return result


class SolutionTest(unittest.TestCase):
    """docstring for SolutionTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
        print "testCase1 3"
        s = Solution()
        # self.assertEquals(s.isPalindrome("a."), True)
        # self.assertEquals(s.isPalindrome("aA"), True)
        # self.assertEquals(s.isPalindrome("a bb"), True )
        result = s.generate(3)
        for x in result:
            print x

    def testCase2(self):
        print "testCase2 1"
        s = Solution()
        result = s.generate(1)
        for  x  in result:
            print x
    def testCase3(self):
        print "testCase3 5"
        s = Solution()
        result = s.generate(5)
        for  x in result:
            print x
    def testCase3(self):
        print "testCase3 2"
        s = Solution()
        result = s.generate(2)
        for  x in result:
            print x
if __name__ == '__main__':
    unittest.main()
        
        
