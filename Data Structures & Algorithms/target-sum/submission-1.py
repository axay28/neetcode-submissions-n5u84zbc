class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for num in nums:
            next=defaultdict(int)
            for t,c in dp.items():
                next[t-num]+=c
                next[t+num]+=c
            dp=next
        return dp[target]