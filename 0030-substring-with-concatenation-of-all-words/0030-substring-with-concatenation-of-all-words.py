class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n=len(words[0])
        m=len(words)
        sl=len(s)
        w=sorted(words)
        f=[]
        k=[]
        for j in range(n):
            k.append([])
            for i in range(j,sl,n):
                k[j].append(s[i:i+n])
        q=len(k)
        for j in range(q):
            qt=len(k[j])
            for i in range(0,qt-m+1):
                t=sorted(k[j][i:i+m])
                if t==w:
                    f.append(i*n+j)
        return list(set(f))
