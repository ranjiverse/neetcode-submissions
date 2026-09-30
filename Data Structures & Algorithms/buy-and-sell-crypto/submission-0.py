class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_b = prices[0]

        for p in prices:
            max_p = max(max_p, p - min_b)
            min_b = min(min_b, p)

        return max_p



        