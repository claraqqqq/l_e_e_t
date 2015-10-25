# Maximum Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		length = len(A)
		sum_arr = [0 for dummy_index in range(length)]
		sum_arr[0] = A[0]
		for index in range(1, length):
			if sum_arr[index - 1] > 0:
				sum_arr[index] = sum_arr[index - 1] + A[index]
			else:
				sum_arr[index] = A[index]
		return max(sum_arr)