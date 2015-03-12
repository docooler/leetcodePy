# Factorial Trailing Zeroes Total Accepted: 15002 Total Submissions: 54588 My Submissions Question Solution 
# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
	# @param A, a list of integer
    # @return an integer
    def trailingZeroes(self,n): 
        ret = 0 
        while n/5:
            ret+=n/5 
            n/=5 
        return ret
