class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob1(nums[1:]),self.rob1(nums[:-1]))
    def rob1(self,nums):
        a,b=0,0
        for num in nums:
            res=max(a+num,b)
            a=b
            b=res
        return b