# Set Matrix Zeroes
# Given a m x n matrix, if an element is 0, set its entire row 
# and column to 0. Do it in place.
# click to show follow up.
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a 
# bad idea.
# A simple improvement uses O(m + n) space, but still not the 
# best solution.
# Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for dummy_idx in range(rownum)]
        col = [False for dummy_idx in range(colnum)]
        for idx in range(rownum):
            for idy in range(colnum):
                if matrix[idx][idy] == 0:
                    row[idx] = True
                    col[idy] = True
        for idx in range(rownum):
            for idy in range(colnum):
                if row[idx] or col[idy]:
                    matrix[idx][idy] = 0