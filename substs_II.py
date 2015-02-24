# Subsets II
# Given a collection of integers that might contain duplicates,S, 
# return all possible subsets.
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result = []
        self.subsetsRecur(result, [], sorted(S))
        return result
    
    def subsetsRecur(self, result, subset, S):
        if len(S) == 0 and subset not in result:
            result.append(subset)
        elif len(S):
            self.subsetsRecur(result, subset, S[1:])
            self.subsetsRecur(result, subset + [S[0]], S[1:])
