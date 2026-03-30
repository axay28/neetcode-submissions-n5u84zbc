class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        opt=[0]*(amount+1)
        opt[0]=1
        for i in range(len(coins)-1,-1,-1):
            for a in range(1,amount+1):
                opt[a]+=opt[a-coins[i]] if coins[i]<=a else 0
        return opt[amount]
        