class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(numRows-1):
            l+=[[1]+[0]*i+[1]]
            if i>=1:
                for j in range(1,i+1):
                    l[-1][j]=l[-2][j-1]+l[-2][j]
        # print(l)
        return l
            
            
        