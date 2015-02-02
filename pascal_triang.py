# Pascal's Triangle
# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        triangle_arr = []
        for idx_row in range(numRows):
            triangle_arr.append([])
            for idx_col in range(idx_row + 1):
                if idx_col == 0 or idx_col == idx_row:
                    triangle_arr[idx_row].append(1)
                else:
                    val = triangle_arr[idx_row-1][idx_col-1] + triangle_arr[idx_row-1][idx_col]
                    triangle_arr[idx_row].append(val)
        return triangle_arr