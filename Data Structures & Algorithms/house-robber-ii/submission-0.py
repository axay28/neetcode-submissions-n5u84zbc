class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob1(nums[1:]),self.rob1(nums[:-1]))
    def rob1(self,nums):
        x,y=0,0
        for num in nums:
            temp=max(x+num,y)
            x=y
            y=temp
        return y