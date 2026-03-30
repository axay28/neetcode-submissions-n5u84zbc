class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=set(nums)
        l=len(nums)
        for i in range(l+1):
            if i not in n:
                return i
        