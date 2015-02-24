# Maximum Product Subarray
# Find the contiguous subarray within an array (containing at 
# least one number) which has the largest product.
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        min_tmp = A[0]
        max_tmp = A[0]
        result = A[0]
        for idx in range(1, len(A)):
            mn = A[idx] * min_tmp
            mx = A[idx] * max_tmp
            cur = A[idx]
            max_tmp = max(max(mn, mx), cur)
            min_tmp = min(min(mn, mx), cur)
            if max_tmp > result:
                result = max_tmp 
        return result
