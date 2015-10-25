# Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all 
# elements of the matrix in spiral order.
# For example,
# Given the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == [] or matrix[0] == []:
            return result
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1 
        while left <= right and top <= bottom:
            for idx in range(left, right + 1):
                result.append(matrix[top][idx])
            for idy in range(top + 1, bottom):
                result.append(matrix[idy][right])
            for idx in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][idx])
            for idy in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[idy][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result