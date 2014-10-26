class Solution:
    # @return an integer
    def reverse(self, x):
        n = abs(x)
        solution = 0
        while n >0:
            solution *= 10
            solution += n%10
            n /= 10
        if x < 0 :
            solution = 0 -solution
        return solution
        