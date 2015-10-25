# 3Sum Closest
# Given an array S of n integers, find three integers in S 
# such that the sum is closest to a given number, target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. 
#     (-1 + 2 + 1 = 2).

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        min_diff = 'Inf'
        res = 0
        for idx in range(len(num)):
            left = idx + 1
            right = len(num) - 1
            while left < right:
                sum = num[idx] + num[left] + num[right]
                diff = abs(sum - target)
                if diff < min_diff: 
                    min_diff = diff
                    res = sum
                if sum == target: 
                    return sum
                elif sum < target: 
                    left += 1
                else: 
                    right -= 1
        return res