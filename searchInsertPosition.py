class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        length = len(A)
        i = 0
        while i< length:
            if A[i] >= target:
                return i
            i += 1
        return i
        
