# Merge Sorted Array
# Given two sorted integer arrays A and B, merge B into A 
# as one sorted array.
# Note:
# You may assume that A has enough space 
# (size that is greater or equal to m + n) to hold additional 
# elements from B. The number of elements initialized in A and 
# B are m andn respectively.

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        
        idx_last =  m + n - 1
        idx_a = m - 1
        idx_b = n - 1
        
        while idx_a >= 0 and idx_b >= 0:
            
            if A[idx_a] > B[idx_b]:
                A[idx_last] = A[idx_a]
                idx_a -= 1
                idx_last -= 1
            else:
                A[idx_last] = B[idx_b]
                idx_b -= 1
                idx_last -= 1
                
        while idx_b >= 0:
            A[idx_last] = B[idx_b]
            idx_b -= 1 
            idx_last -= 1
