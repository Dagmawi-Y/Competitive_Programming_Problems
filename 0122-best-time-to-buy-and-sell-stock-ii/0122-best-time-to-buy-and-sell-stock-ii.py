class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            if i < len(prices) - 1 and prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit
            