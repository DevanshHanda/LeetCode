class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        t = Counter(arr)
        c=0
        for j in t:
            if t[j]==1:
                c+=1
                if c==k:
                    return j
        
        return ''