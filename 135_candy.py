# Candy
# There are N children standing in a line. 
# Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# 
#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.
# 
# What is the minimum candies you must give?

class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		candy_rcrd = [1 for dummy_index in range(len(ratings))]
		
		for index in range(1, len(ratings)):
			if ratings[index] > ratings[index - 1]:
				candy_rcrd[index] = candy_rcrd[index - 1] + 1
		
		for index in range(len(ratings) - 2, -1, -1):
			if ratings[index] > ratings[index + 1]:
				if candy_rcrd[index] <= candy_rcrd[index + 1]:
					candy_rcrd[index] = candy_rcrd[index + 1] + 1
		
		return sum(candy_rcrd)