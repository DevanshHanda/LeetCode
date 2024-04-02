class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i,j in enumerate(s):
            if j not in d:
                if t[i] not in d.values():
                    d[j]=""
                    d[j]=t[i]
                else:
                    return False
            else:
                if d[j]!=t[i]:
                    return False
            # print(d)
        return True
            
                