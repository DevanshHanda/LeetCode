class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        m = max(arr)
        i = arr.index(m)
        if i==0 or i==len(arr)-1:
            return False
        for j in range(i):
            if arr[j]>=arr[j+1]:
                return False
        for j in range(i,len(arr)-1):
            if arr[j+1]>=arr[j]:
                return False
        return True
            
                