class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            j = i + 1
            while j < len(prices) and prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i]) 
                j += 1
            i = j
        return max_profit