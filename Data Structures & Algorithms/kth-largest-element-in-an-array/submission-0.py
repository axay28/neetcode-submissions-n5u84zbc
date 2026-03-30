class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        pivot=nums[0]
        left=[x for x in nums[1:] if x>pivot]
        right=[x for x in nums[1:]if x<=pivot]
        L=len(left)
        if k<=L:
            return self.findKthLargest(left,k)
        elif k==L+1:
            return pivot
        else:
            return self.findKthLargest(right,k-L-1)