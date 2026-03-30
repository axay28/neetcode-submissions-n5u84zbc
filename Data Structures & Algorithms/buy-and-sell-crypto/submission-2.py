class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minb=prices[0]
        profit=0
        for p in prices:
            profit=max(profit,p-minb)
            minb=min(minb,p)
        return profit
