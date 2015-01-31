# String to Integer (atoi)
# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. 
# If you want a challenge, please do not see below and 
# ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified 
# vaguely (ie, no given input specs). 
# You are responsible to gather all the input requirements 
# up front.

# Requirements for atoi:
# The function first discards as many whitespace characters 
# as necessary until the first non-whitespace character is 
# found. Then, starting from this character, takes an optional 
# initial plus or minus sign followed by as many numerical 
# digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those 
# that form the integral number, which are ignored and have 
# no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str 
# is not a valid integral number, or if no such sequence exists 
# because either str is empty or it contains only whitespace 
# characters, no conversion is performed.
# If no valid conversion could be performed, 
# a zero value is returned. If the correct value is out of the 
# range of representable values, INT_MAX (2147483647) or 
# INT_MIN (-2147483648) is returned.

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str_new = []
        for i in xrange(len(str)):
            if '0' <= str[i] <= '9' or (str[i] in '+-' and i == 0):
                str_new.append(str[i])
            else:
                break
        if str_new in [[],['+'],['-']]:
            return 0
        int_new = int(''.join(str_new))
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if int_new >= INT_MIN and int_new <= INT_MAX:
            return int_new
        elif int_new > INT_MAX:
            return INT_MAX
        else:
            return INT_MIN