class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = 46340 # sqrt(C MAX_INT 2147483647)=46340.950001
        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
