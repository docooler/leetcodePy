class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        length = len(prices)
        i = 0
        while i < length:
            j=i
            max = 0
            for j in range(length):
                temp = prices[j] - prices[i]
                if temp > max :
                    max = temp
            if max > profit:
                profit = max
            i += 1
        return profit
            
        
