# Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is 
# the price of a given stock on day i.
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for current_price in prices:
            min_price = min(current_price, min_price)
            max_profit = max(max_profit, current_price-min_price)
        return max_profit