class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy=prices[0]
        maxprofit=0
        for p in prices:
            maxprofit=max(maxprofit,p-minbuy)
            minbuy=min(minbuy,p)

        return maxprofit