Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        leftMostHigh = [0 for dummy_idx in range(len(A))]
        leftMax = 0
        for idx in range(len(A)):
            if A[idx] > leftMax: 
                leftMax = A[idx]
            leftMostHigh[idx] = leftMax
        sum = 0
        rightMax = 0
        for idx in reversed(range(len(A))):
            if A[idx] > rightMax: 
                rightMax = A[idx]
            if min(rightMax, leftMostHigh[idx]) > A[idx]:
                sum += min(rightMax, leftMostHigh[idx]) - A[idx]
        return sum