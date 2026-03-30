class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        maxP=0
        for p in prices:
            maxP=max(maxP,p-minimum)
            minimum=min(minimum,p)
        return maxP
        