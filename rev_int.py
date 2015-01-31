# Reverse Integer
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# Have you thought about this?

class Solution:
    # @return an integer
    def reverse(self, x):
        x_str = str(x)
        if x_str[0] != '-':
            return int(x_str[::-1])
        else:
            return int('-' + x_str[-1:0:-1])
