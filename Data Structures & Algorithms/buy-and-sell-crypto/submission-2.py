class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')

        for price in prices:
            if price < min_buy:
                min_buy = price
            
            elif price - min_buy > max_profit:
                max_profit = price - min_buy

        return max_profit