class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini,maxi,res=1,1,nums[0]
        for n in nums:
            t=maxi*n
            maxi=max(n*maxi,n*mini,n)
            mini=min(n,n*mini,t)
            res=max(res,maxi)
        return res

        