class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1,sell1,buy2=0,0,0
        n=len(prices)
        for i in range(n-1,-1,-1):
            buy=max(sell1-prices[i],buy1)
            sell=max(sell1,buy2+prices[i])
            buy2=buy1
            buy1,sell1=buy,sell
        return buy1        