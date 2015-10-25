# Plus One
# Given a non-negative number represented as an array of digits, 
# plus one to the number.
# The digits are stored such that the most significant digit 
# is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        #for i in reversed(range(len(digits))):  
        for i in range(len(digits)-1, -1, -1):
            digit_sum = digits[i] + carry
            digits[i] = digit_sum % 10
            carry = digit_sum / 10
        if carry:
            digits = [1] + digits
        return digits