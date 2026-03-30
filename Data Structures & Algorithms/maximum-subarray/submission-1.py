class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        maxs=nums[0]
        for num in nums:
            if cursum<0:
                cursum=0
            cursum+=num
            maxs=max(maxs,cursum)
        return maxs