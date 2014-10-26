class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        length = len(digits)-1
        carrier = 1
        while carrier == 1 and length >= 0:
            num = carrier + digits[length]
            digits[length] = num%10
            carrier = num/10
            length -= 1
        if carrier == 1:
            digits.insert(0,1)
        return digits