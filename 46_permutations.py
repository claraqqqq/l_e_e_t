# Permutations
# Given a collection of numbers, return all possible permutations.
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        length = len(num)
        if length == 0:
            return []
        if length == 1:
            return [num]
        result = []
        for idx in range(length):
            for rest_perm in self.permute(num[0:idx] + num[idx+1:]):
                result.append([num[idx]] + rest_perm)
        return result
