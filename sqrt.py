class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        low = 0.0
        up  = x
        min = (low+up)/2
        while True:
            power = min**2
            if power > x:
                up = min
            else:
                low = min
            last = min
            min = (up+low)/2
            if abs(min-last) < 0.00000000000000005:
                break
        return int(min)
        
