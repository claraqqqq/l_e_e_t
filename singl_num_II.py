# Single Number II
# Given an array of integers, every element appears three 
# times except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = {}
        for item in A:
            if item not in result.keys():
                result[item] = 1
            else:
                result[item] += 1
        for key in result.keys():
            if result[key] == 1:
                return key