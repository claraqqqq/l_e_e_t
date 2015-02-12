# Unique Paths II
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. 
# How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 
# respectively in the grid.
# For example,
# There is one obstacle in the middle of a 3x3 grid as 
# illustrated below.
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# Note: m and n will be at most 100.

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        numRow = len(obstacleGrid) 
        numCol = len(obstacleGrid[0])
        ways = [[0 for dummy_idy in range(numCol)] for dummy_idx in range(numRow)]
        for idxRow in range(numRow):
            for idxCol in range(numCol):
                if obstacleGrid[idxRow][idxCol] == 0:
                    if idxRow == 0 and idxCol == 0:
                        ways[idxRow][idxCol] = 1
                    elif idxRow == 0:
                        ways[idxRow][idxCol] = ways[idxRow][idxCol-1]
                    elif idxCol == 0:
                        ways[idxRow][idxCol] = ways[idxRow-1][idxCol]
                    else:
                        ways[idxRow][idxCol] = ways[idxRow-1][idxCol] + ways[idxRow][idxCol-1]
        return ways[numRow-1][numCol-1]