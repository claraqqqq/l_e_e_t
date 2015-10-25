# Triangle
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        
        length = len(triangle)
        sum_rcrd = [0 for dummy_index in range(length)]
        
        for row_item in triangle:
            sum_rcrd_tmp = sum_rcrd[:]
            for index in range(len(row_item)):
                if index == 0:
                    sum_rcrd[index] = sum_rcrd_tmp[index] + row_item[index]
                elif index == len(row_item) - 1:
                    sum_rcrd[index] = sum_rcrd_tmp[index-1] + row_item[index]
                else:
                    sum_rcrd[index] = min(sum_rcrd_tmp[index-1], sum_rcrd_tmp[index]) + row_item[index]  
        
        return min(sum_rcrd)