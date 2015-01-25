# Sqrt(x)
# Implement int sqrt(int x).
# Compute and return the square root of x.

class Solution:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		high = x
		low = 0
		mid = high
		label = True
		while label:
			if mid ** 2 <= x and (mid+1) ** 2 > x:
				label = False
				continue
			elif mid ** 2 < x:
				low = mid
			elif mid ** 2 > x:
				high = mid
				mid = int((high + low) / 2)
		return mid