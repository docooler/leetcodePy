import unittest

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        
        first   = 0
        second  = 1
        for i in range(n):
            first, second = second, second + first

        return second
class SolutionTest(unittest.TestCase):
    """docstring for SolutionTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testCase1(self):
        s = Solution()
        self.assertEquals(s.climbStairs(1), 1)
        self.assertEquals(s.climbStairs(2), 2)
        self.assertEquals(s.climbStairs(3), 3)
        print s.climbStairs(5)
        print s.climbStairs(10)
if __name__ == '__main__':
    unittest.main()
        
