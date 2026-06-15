class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = 101
        lowestIndex = 0
        for index, price in enumerate(prices):
            if price < lowest:
                lowest = price
                lowestIndex = index
            profit = max(profit, price - lowest)
        return profit