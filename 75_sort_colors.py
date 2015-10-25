# Sort Colors
# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, 
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the 
# color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for 
# this problem.
# click to show follow up.
# Follow up:
# A rather straight forward solution is a two-pass algorithm 
# using counting sort.
# First, iterate the array counting number of 0's, 1's, and 
# 2's, then overwrite array with total number of 0's, then 1's 
# and followed by 2's.
# Could you come up with an one-pass algorithm using only 
# constant space?


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []: 
            return 
        p0 = 0
        p2 = len(A) - 1
        idx = 0
        while idx <= p2:
            if A[idx] == 2:
                tmp = A[idx]
                A[idx] = A[p2]
                A[p2] = tmp
                p2 -= 1
            elif A[idx] == 0:
                tmp = A[idx]
                A[idx] = A[p0]
                A[p0] = tmp
                p0 += 1
                idx += 1
            else:
                idx += 1
