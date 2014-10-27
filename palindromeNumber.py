class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        num = x
        target = 0
        while num > 0:
            mod = num %10
            target *= 10
            target += mod
            num /= 10
        if target == x:
            return True
        return False
