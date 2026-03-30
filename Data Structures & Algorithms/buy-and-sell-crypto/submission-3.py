class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprofit=prices[0]
        for p in prices:
            maxprofit=max(maxprofit,p-minprofit)
            minprofit=min(minprofit,p)
        return maxprofit            