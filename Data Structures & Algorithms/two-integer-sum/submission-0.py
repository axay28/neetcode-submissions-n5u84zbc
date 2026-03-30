class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for v,i in enumerate(nums):
            difference=target-i
            if difference in map:
                return [map[difference],v]
            map[i]=v
        