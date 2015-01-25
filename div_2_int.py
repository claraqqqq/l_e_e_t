# Divide Two Integers
# Divide two integers without using multiplication, division 
# and mod operator.

class Solution:
	# @return an integer
	def divide(self, dividend, divisor):
		if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
			sign = 1
		else:
			sign = -1
		dividend = abs(dividend)
		divisor = abs(divisor)
		quotient = 0
		while dividend >= divisor:
			cnt = 0
			temp_divisor = divisor
			while dividend >= temp_divisor:
				quotient += (1 << cnt)
				dividend -= temp_divisor
				temp_divisor <<= 1
				cnt += 1
		return quotient * sign