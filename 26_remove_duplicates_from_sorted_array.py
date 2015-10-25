# Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such 
# that each element appear only once # and return the new length.
# Do not allocate extra space for another array, you must do this 
# in place with constant memory.
# For example,
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        idx_unique = 0
        for idx in range(1, len(A)):
            if A[idx_unique] != A[idx]:
                idx_unique += 1
                A[idx_unique] = A[idx]
        #idx = idx_unique
        #while len(A) != idx_unique + 1:            
        #    A.remove(A[idx])
        return idx_unique + 1