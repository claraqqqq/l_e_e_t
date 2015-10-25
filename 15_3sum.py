# 3Sum
# Given an array S of n integers, are there elements a, b, # c in S such that a + b + c = 0? Find all unique triplets 
# in the array which gives the sum of zero.
# Note:
# Elements in a triplet (a,b,c) must be in non-descending 
# order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
# 
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = []
        for idx in range(len(num)-2):
            if idx == 0 or num[idx] > num[idx-1]:
                left = idx + 1; 
                right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[idx]:
                        res.append([num[idx], num[left], num[right]])
                        left += 1; 
                        right -= 1
                        while left < right and num[left] == num[left-1]: 
                            left += 1
                        while left < right and num[right] == num[right+1]: 
                            right -= 1
                    elif num[left] + num[right] < -num[idx]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: 
                                break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]:
                                break
        return res