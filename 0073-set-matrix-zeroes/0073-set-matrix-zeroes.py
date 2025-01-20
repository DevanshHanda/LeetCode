class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        locs = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    locs.append([i,j])
        # print(locs)
        for i,j in locs:
            for a in range(len(matrix)):
                matrix[a][j]=0
                for b in range(len(matrix[a])):
                    matrix[i][b]=0
        # print(matrix)


                

