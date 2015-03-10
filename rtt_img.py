# Rotate Image
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Follow up:
# Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for idx in range(n):
            for idy in range(idx+1, n):
                tmp = matrix[idx][idy]
                matrix[idx][idy] = matrix[idy][idx]
                matrix[idy][idx] = tmp
        for idx in range(n):
            matrix[idx].reverse()
        return matrix