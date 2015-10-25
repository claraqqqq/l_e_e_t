# 4Sum
# Given an array S of n integers, are there elements a, b, 
# c, and d in S such that a + b + c + d = target? Find all 
# unique quadruplets in the array which gives the sum of 
# target.
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-
# descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
#    For example, given array S = {1 0 -1 0 -2 2}, and 
#    target = 0.
#
#    A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    
    def fourSum(self, num, target):
        length = len(num)
        result = set()
        dict_2sum = {}
        if length < 4: 
            return []
        num.sort()
        for idx in range(length):
            for idy in range(idx+1, length): 
                if num[idx] + num[idy] not in dict_2sum:
                    dict_2sum[num[idx] + num[idy]] = [(idx, idy)]
                else:
                    dict_2sum[num[idx] + num[idy]].append((idx, idy))
        for id1 in range(length):
            for id2 in range(id1+1, length-2):
                residual = target - num[id1] - num[id2]
                if residual in dict_2sum:
                    for idset in dict_2sum[residual]:
                        if idset[0] > id2: 
                            result.add((num[id1], num[id2], num[idset[0]], num[idset[1]]))
        return [list(dummy_set) for dummy_set in result]
