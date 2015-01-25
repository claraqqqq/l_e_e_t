# Max Points on a Line
# Given points on a 2D plane, find the maximum number of 
# points that lie on the same straight line.

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        length = len(points)

        if length <= 2:
        	return length
        
        max_num = -1
        
        for idx1 in range(length):

        	slope = dict()
        	same_point_cnt = 0
        	num1 = points[idx1]

        	for idx2 in range(length):

        		num2 = points[idx2]

        		# same index
        		if idx1 == idx2:
        			continue

        		# same points
        		if num1.x == num2.x and num1.y == num2.y:
        			same_point_cnt += 1
        			slope['same_point'] = 0


        		# inf slope points
        		elif num1.x == num2.x and num1.y != num2.y:
        			if 'inf' not in slope.keys():
        				slope['inf'] = 1
        			else:
        				slope['inf'] += 1

        	    # normal slope
        		else:
        			k = (num1.y-num2.y) / float(num1.x-num2.x)
        			if k not in slope.keys():
        				slope[k] = 1
        			else:
        				slope[k] += 1

        	max_num = max(max_num, max(slope.values())+same_point_cnt+1)
        return max_num
        			

