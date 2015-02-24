# Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a 
# path from top left to bottom right which minimizes the sum of 
# all numbers along its path.
# Note: You can only move either down or right at any point in 
# time.

class Solution:
    
    # @param grid, a list of lists of integers
    # @return an integer
    
    def minPathSum(self, grid):
        
        numRow = len(grid)
        numCol = len(grid[0])
        
        for idxRow in range(1, numRow):
            grid[idxRow][0] += grid[idxRow-1][0]
            
        for idxCol in range(1, numCol):
            grid[0][idxCol] += grid[0][idxCol-1]
            
        for idxRow in range(1, numRow):
            for idxCol in range(1, numCol):
                grid[idxRow][idxCol] += min(grid[idxRow-1][idxCol], grid[idxRow][idxCol-1])
                
        return grid[-1][-1]