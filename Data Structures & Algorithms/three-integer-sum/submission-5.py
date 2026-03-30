class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for index,num in enumerate(nums):
            if num>0:
                break
            if num==nums[index-1] and index>0:
                continue
            l,r=index+1,len(nums)-1
            while l<r:
                threesum=num+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
            

        return res
