class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buy=prices[0]
        for price in prices:
            maxProfit=max(maxProfit,price-buy)
            buy=min(buy,price)
        return maxProfit

