# Next Permutation
# Implement next permutation, which rearranges numbers into 
# the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it 
# as the lowest possible order (ie, sorted in ascending 
# order).
# The replacement must be in-place, do not allocate extra 
# memory.
# Here are some examples. Inputs are in the left-hand 
# column and its corresponding outputs are in the right-# hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1: 
            return num
        partition = -1
        label = 0
        for idx in range(len(num) - 1):
            if num[idx] < num[idx+1]:
                partition = idx
        if partition == -1:
            return num[::-1]
        for idx in range(len(num)):
            if num[idx] > num[partition]:
                label = idx
        tmp = num[partition]       
        num[partition] = num[label] 
        num[label] = tmp
        return num[:partition+1] + num[:partition:-1]
