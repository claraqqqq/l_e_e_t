# Roman to Integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        numerals_dict = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum = 0
        numeral_prev = None
        for key in s:
            if numeral_prev != None and numeral_prev < numerals_dict[key]:
                sum -= 2*numeral_prev
            sum += numerals_dict[key]
            numeral_prev = numerals_dict[key]
        return sum