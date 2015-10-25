# Roman to Integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        prev = None
        
        for key in s:
            if prev!=None and prev<dic[key]:
                res -= 2*prev
            res += dic[key]
            prev = dic[key]
        
        return res
