# Anagrams
# Given an array of strings, return all groups of strings that 
# are anagrams.
# Note: All inputs will be in lower-case.
# An anagram is a type of word play, the result of rearranging 
# the letters of a word or phrase to produce a new word or 
# phrase, using all the original letters exactly once; for 
# example Torchwood can be rearranged into Doctor Who.


class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord  not in dict:
                dict[sortedWord] = [word]
            else: 
                dict[sortedWord] += [word]
        result = []
        for key in dict:
            if len(dict[key]) >= 2:
                result += dict[key]
        return result