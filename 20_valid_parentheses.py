# Valid Parentheses

'''
Given a string containing just the characters '(', ')','{', 
'}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]
{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        lookup = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if len(stack) == 0 or lookup[stack.pop()] != char:
                    return False
        return len(stack) == 0