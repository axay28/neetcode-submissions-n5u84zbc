class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def dfs(x,y):
            if x==y==n:
                res.append("".join(stack))
                return
            if x<n:
                stack.append("(")
                dfs(x+1,y)
                stack.pop()
            if y<x:
                stack.append(")")
                dfs(x,y+1)
                stack.pop()
        dfs(0,0)
        return res
        