# Search for a Range
# Given a sorted array of integers, find the starting and 
# ending position of a given target value.
# Your algorithm's runtime complexity must be in the order 
# of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                result = [0, 0]
                if A[left] == target: 
                    result[0] = left
                if A[right] == target: 
                    result[1] = right
                for idx in range(mid, right+1):
                    if A[idx] != target: 
                        result[1] = idx - 1
                        break
                for idx in range(mid, left-1, -1):
                    if A[idx] != target: 
                        result[0] = idx + 1  
                        break
                return result
        return [-1, -1]