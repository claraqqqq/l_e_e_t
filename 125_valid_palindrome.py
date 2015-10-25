# Valid Palindrome
# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# Note:
# Have you consider that the string might be empty? 
# This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as 
# valid palindrome.

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        result = []
        for letter in s:
            if '0' <= letter <= '9' or 'a' <= letter <= 'z':
                result.append(letter)
            elif 'A' <= letter <= 'Z':
                result.append(chr(ord(letter) - ord('A') + ord('a')))
        return result == result[::-1]