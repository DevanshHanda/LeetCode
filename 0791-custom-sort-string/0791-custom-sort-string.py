class Solution:
    def customSortString(self, order: str, s: str) -> str:
        o = set([x for x in order])
        st = set([x for x in s])
        t = o&st
        af = st - o
        k=''
        s = [x for x in s]
        for i in order:
            if i in t:
                k+=i
                s.remove(i)
        for i in s:
            if i in t:
                k = k[:k.index(i)]+i+k[k.index(i):]
            if i in af:
                k+=i
        
        return k
