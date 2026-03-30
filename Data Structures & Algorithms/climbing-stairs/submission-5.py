class Solution:
    def climbStairs(self, n: int) -> int:
        x,y=1,1
        for i in range(n):
            temp=x
            x=x+y
            y=temp
        return y