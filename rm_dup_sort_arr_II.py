# Remove Duplicates from Sorted Array II
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# Your function should return length = 5, and A is now 
# [1,1,2,2,3].


class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length == 0: 
            return 0
        idx_update = 0
        same_cnt = 1
        for idx in range(1, length):
            if A[idx] == A[idx - 1]:
                same_cnt += 1
                if same_cnt <= 2:
                    idx_update += 1
                    A[idx_update] = A[idx]
            else:
                same_cnt = 1
                idx_update += 1
                A[idx_update] = A[idx]
        return idx_update + 1


class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        idx = 0
        same_cnt = 0
        for idy in range(1, len(A)):
            if A[idx] != A[idy] or same_cnt == 0:
                same_cnt = A[idx] == A[idy]
                idx += 1
                A[idx] = A[idy]
        return idx + 1