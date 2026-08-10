class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, max_profit = 0,0
        for end in range(1, len(prices)):
            max_profit = max(max_profit, prices[end]-prices[start])
            if(prices[end] < prices[start]):
                start = end
        return max_profit

        