class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in 2*nums:
            ans.append(num)
        return ans