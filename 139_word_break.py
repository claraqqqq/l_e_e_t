# Word Break
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
    """
    Dynamic programming:
    Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. 
    It is applicable to problems exhibiting the properties of overlapping subproblems[1] and optimal substructure.
    In general, to solve a given problem, we need to solve different parts of the problem (subproblems), then combine 
    the solutions of the subproblems to reach an overall solution,
    Often when using a more naive method, many of the subproblems are generated and solved many times. 
    The dynamic programming approach seeks to solve each subproblem only once, thus reducing the number of computations: 
    once the solution to a given subproblem has been computed, it is stored or "memo-ized": the next time the same solution 
    is needed, it is simply looked up. 
    """
        length = len(s)
        rcrd = [False for dummy_idx in range(length+1)]
        rcrd[0] = True
        for break_idx in range(1, length+1):
            for tmp_break_idx in range(break_idx):
                if rcrd[tmp_break_idx] == True and \
                   s[tmp_break_idx : break_idx] in dict:
                    rcrd[break_idx] = True
                    break
        return rcrd[-1]  
