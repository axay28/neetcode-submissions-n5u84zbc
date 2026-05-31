class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in 2*nums:
            ans.append(i)
        return ans