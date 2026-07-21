class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_sell = 0
        max_profit = 0

        for price in reversed(prices):
            if price > max_sell:
                max_sell = price 
            profit = max_sell - price

            if profit > max_profit:
                max_profit = profit
            
        return max_profit