# Spiral Matrix II
# Given an integer n, generate a square matrix filled with 
# elements from 1 to n2 in spiral order.
# For example,
# Given n = 3,
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    # @return a list of lists of integer 
    def generateMatrix(self, n):
        matrix = [[0 for dummy_idx in range(n)] for dummy_idx in range(n)]
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        num = 1
        while left <= right and top <= bottom:
            for idx in range(left, right + 1):
                matrix[top][idx] = num
                num += 1
            for idy in range(top + 1, bottom):
                matrix[idy][right] = num
                num += 1
            for idx in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][idx] = num
                    num += 1
            for idy in reversed(range(top + 1, bottom)):
                matrix[idy][left] = num
                num += 1
            left += 1 
            right -= 1
            top += 1
            bottom -= 1
        return matrix