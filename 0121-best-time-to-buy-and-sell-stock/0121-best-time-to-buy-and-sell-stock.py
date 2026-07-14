class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        cheapest_so_far=prices[0] # say for now 
        proft_if_sold_today=0
        max_profit=0 # say 

        for current_price in prices:
            if current_price <= cheapest_so_far:
                cheapest_so_far= current_price #updated
            
            profit_if_sold_today= current_price - cheapest_so_far

            if profit_if_sold_today >= max_profit:
                max_profit = profit_if_sold_today
        return max_profit
