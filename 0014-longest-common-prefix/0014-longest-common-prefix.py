class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs)
        f=True
        k=''
        for i in range(len(m)):
            for j in strs:
                if m[i]!=j[i]:
                    f=False 
            if not f:
                return k
            k+=m[i]
        return k




            