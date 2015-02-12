# Unique Paths
# A robot is located at the top-left corner of a m x n grid 
# (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point 
# in time. The robot is trying to reach the bottom-right 
# corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Note: m and n will be at most 100.

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        ways = [[1] for dummy_idx in range(m)]
        for dummy_idx in range(1, n):
            ways[0].append(1)
        for idx_row in range(1, m):
            for idx_col in range(1, n):
                ways[idx_row].append(ways[idx_row-1][idx_col] + ways[idx_row][idx_col-1])
        return ways[m-1][n-1]