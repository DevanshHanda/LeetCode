class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        a = []
        ind = 0
        for i in range(m):
            a.append(original[ind:ind+n])
            ind+=n
        # print(a)
        return a