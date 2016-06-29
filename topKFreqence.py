class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        dataHash = {}
        for x in nums:
            if dataHash.has_key(x):
                dataHash[x] += 1
            else:
                dataHash[x] = 1
                
        freqHash = {}
        for x in dataHash.keys():
            freq = dataHash[x]
            if freqHash.has_key(freq):
                freqHash[freq].append(x)
            else:
                freqHash[freq] = [x]
                
                
        freqList =[]
        for x in freqHash.keys():
            freqList.append(x)
        freqList.sort()
        freqList.reverse()

        print freqList
        
        result =[]
        cnt = 0
        for x in freqList:
            datas = freqHash[x]
            print str(x) + ":" 
            print datas
            for data in datas:
                result.append(data)
                cnt += 1
                if cnt == k:
                    return result
               
        return result

import unittest
class SolutionUnitTest(unittest.TestCase):
    """docstring for SolutionUnitTest"""
    def setup(self):
        pass
    def tearDown(self):
        pass

    def test1(self):
        s = Solution()
        nums = [1,1,1,2,2,3]
        print s.topKFrequent(nums, 2);
if __name__ == '__main__':
    unittest.main()
