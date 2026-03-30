class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])
        newrows,newcols=[False]*rows,[False]*cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    newrows[r]=True
                    newcols[c]=True
        for r in range(rows):
            for c in range(cols):
                if newrows[r] or newcols[c]:
                    matrix[r][c]=0
