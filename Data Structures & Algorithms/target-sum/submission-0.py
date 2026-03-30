class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        opt=defaultdict(int)
        opt[0]=1
        for n in nums:
            next=defaultdict(int)
            for t,c in opt.items():
                next[t+n]+=c
                next[t-n]+=c
            opt=next
        return opt[target]