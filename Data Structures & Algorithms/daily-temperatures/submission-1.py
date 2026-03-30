class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res, stack = [0]*N, []  
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                x, y = stack.pop()
                res[y] = i - y
            stack.append((t, i))
        return res
