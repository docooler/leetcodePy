class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 2:
            return 1
        ways = [0] * (n+1)
        ways[0] = 0
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways[i-2] + ways[i-1]
        return ways[n]
