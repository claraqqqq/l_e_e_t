# Best Time to Buy and Sell Stock III
# Say you have an array for which the ith element is 
# the price of a given stock on day i.
# Design an algorithm to find the maximum profit. 
# You may complete at most two transactions.
# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        
        length = len(prices)
        
        if length == 0:
             return 0
             
        max_profit_forward = []     
        max_profit1 = 0
        min_price = prices[0]
        for current_price in prices:
            min_price = min(min_price, current_price)
            max_profit1 = max(max_profit1, current_price-min_price)
            max_profit_forward.append(max_profit1)
        
        max_profit_backward = []
        max_profit2 = 0
        max_price = prices[-1]
        for current_price in reversed(prices):
            max_price = max(max_price, current_price)
            max_profit2 = max(max_profit2, max_price-current_price)
            max_profit_backward.insert(0, max_profit2)
            
        max_profit = max_profit_forward[-1]
        for index in range(length-1):
            max_profit = max(max_profit, max_profit_forward[index] + max_profit_backward[index+1])
            
        return max_profit