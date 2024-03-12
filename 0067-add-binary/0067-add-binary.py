class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na=int(a,2)
        nb=int(b,2)
        nc = nb+na
        return "{0:b}".format(nc)
