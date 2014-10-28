import unittest

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        first   = 1
        second  = 2
        for i in range(n-2):
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
if __name__ == '__main__':
    unittest.main()
        
