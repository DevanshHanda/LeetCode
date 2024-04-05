class Solution:
    def makeGood(self, s: str) -> str:
        s=s[::-1]
        l=["$"]
        for i,x in enumerate(s):
            if l[-1]!=x:
                if l[-1].upper() == x or l[-1].lower() == x:
                    l.pop()
                else:
                    l.append(x)
            else:
                l.append(x)
        t = ''.join(l[::-1])
        return t[:-1]


            
