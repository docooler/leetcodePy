Line 18: RuntimeError: maximum recursion depth exceeded in cmp
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return True
        self.travel = ['u'] * len(nums)
        self.nums = nums
        self.length = len(nums)
        return self.startTravel(0)
    def startTravel(self, start):
        flag = False
        if start >= self.length-1:
            return True
        
        if self.travel[start] == 'u':
            for x in xrange(self.nums[start]):
                if self.startTravel(start+x+1) == True:
                    flag = True
            self.travel[start] = flag
        return self.travel[start]
        
        
