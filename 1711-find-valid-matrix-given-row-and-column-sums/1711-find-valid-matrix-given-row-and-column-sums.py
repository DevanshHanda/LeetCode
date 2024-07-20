# from sympy import *
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)

        mat = []
        for i in range(m):
            mat.append([])
            for j in range(n):
                t = min(rowSum[i],colSum[j])
                mat[i].append(t)
                rowSum[i]-=t
                colSum[j]-=t
        return mat
        



        
        
            

