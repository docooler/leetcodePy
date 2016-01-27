class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
    
        lists = []
        lists.append(1)
        pLen = len(primes)
        idxList = [0] * pLen

        for i in xrange(1, n):
            tempList = []
            for j in xrange(pLen):
                tempList.append(lists[idxList[j]] * primes[j])

            tempMin = min(tempList)
            lists.append(tempMin)
            for k, v in enumerate(tempList):
                if v == tempMin:
                    idxList[k]=idxList[k]+1

        return lists[n-1]
        
        
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
    
        lists = []
        lists.append(1)
        pLen = len(primes)
        idxList = [0] * pLen
        tempList = primes[:]
        for i in xrange(1, n):
            tempMin = min(tempList)
            lists.append(tempMin)
            for k, v in enumerate(tempList):
                if v == tempMin:
                    idxList[k]=idxList[k]+1
                    tempList[k]=lists[idxList[k]]*primes[k]

        return lists[n-1]
