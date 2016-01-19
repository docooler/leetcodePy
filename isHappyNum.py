class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numSet = set()
        sum = n
        while 1:
            numSet.add(sum)
            sum = self.calcSum(sum)
            if sum == 1:
                return True
            if sum in numSet:
                return False
        
            
    def calcSum(self, n):
        sum = 0
        while n != 0:
            sum += (n%10)**2
            n /= 10
        return sum
        
