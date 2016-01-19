class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numMap = {}
        for idx, value in enumerate(nums):
            if value in numMap:
                if idx-numMap[value] < k+1:
                    return True
            numMap[value]=idx
        return False
