class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            n = len(nums)
            if n <= 0: return 0
            maxFirst = [0] * n
            maxLast = [0] * n
            maxFirst[0] = nums[0]
            maxLast[0] = 0
            for i in range(1, n):
                if i - 2 >= 0:
                    maxFirst[i] = max(maxFirst[i-1], maxFirst[i-2]+nums[i])
                    maxLast[i] = max(maxLast[i-1], maxLast[i-2]+nums[i])
                else:
                    maxFirst[i] = max(maxFirst[i-1], nums[i])
                    maxLast[i] = max(maxLast[i-1], nums[i])

            maxFirst[-1] = maxFirst[n-2]
            # the max value is the maximum of these two lists
            return max(max(maxFirst), max(maxLast))
