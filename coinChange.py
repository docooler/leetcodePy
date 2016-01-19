class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins= sorted(coins, reverse=True)
        maxCnt = amount/coins[-1] + 1
        self.length = maxCnt
        if amount == 0:
            return 0
        self.calcCoin(0, amount)
        if self.length == maxCnt:
            return -1
        return self.length
        
    def calcCoin(self,cnt, amount):
        if amount < 0 :
            return
        
        cnt += 1
        if cnt > self.length:
            return
        
        if amount in self.coins:
            if cnt < self.length:
                self.length = cnt
            return
        for coin in self.coins:
            self.calcCoin(cnt, amount-coin)
        
        
        
