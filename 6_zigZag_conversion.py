# ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on 
# a given number of rows like this: (you may want to display 
# this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion 
# given a number of rows:
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        step = 2 * nRows - 2
        zigzag = ""
        if s == None or len(s) == 0 or nRows <= 0:
            return ""
        elif nRows == 1:
            return s
        else:
            for idx_row in range(nRows):
                for idx in range(idx_row, len(s), step):
                    zigzag += s[idx]
                    if idx_row > 0 and idx_row < nRows - 1 and idx + step - 2*idx_row < len(s):
                        zigzag += s[idx + step - 2*idx_row]
            return zigzag