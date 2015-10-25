# Longest Common Prefix
# Write a function to find the longest common prefix 
# string amongst an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        strs_len = len(strs)
        if strs_len == 0:
            return ''
        if strs_len == 1:
            return strs[0]
        strs_len_arr = [len(single_str) for single_str in strs]
        common_prefix = ''
        for idx_letter in range(min(strs_len_arr)):
            common_letter = strs[0][idx_letter]
            for idx_strs in range(1, strs_len):
                if strs[idx_strs][idx_letter] != common_letter:
                    return common_prefix
            common_prefix += common_letter
        return common_prefix