class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest=current=0
        for num in nums:
            if num==0:
                longest=max(longest,current)
                current=0
            else:
                current+=1
        return max(current,longest)
            