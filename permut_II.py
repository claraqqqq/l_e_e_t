# Permutations II
# Given a collection of numbers that might contain duplicates,
# return all possible unique permutations.
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		length = len(num)
		if length == 0:
			return []
		elif length == 1:
			return [num]
		num.sort()
		prev_num = None
		result = []
		for index in range(length):
			if num[index] == prev_num:
				continue
			else:
				prev_num = num[index]
		for perm in self.permuteUnique(num[0 : index] + num[index+1 :]):
			result.append([num[index]] + perm)
		return result