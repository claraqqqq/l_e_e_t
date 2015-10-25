# Pascal's Triangle II
# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3,
# Return [1,3,3,1].
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        triangle_arr_row = [1]
        for idx in range(1, rowIndex + 1):
            triangle_arr_row = [1] + [triangle_arr_row[idy-1] + triangle_arr_row[idy] for idy in range(1, idx)] + [1]
        return triangle_arr_row