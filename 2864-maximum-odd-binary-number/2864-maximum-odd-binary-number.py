class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = [x for x in s]
        t = l.count('1')
        e = l.count('0')
        return (t-1)*'1'+e*'0'+'1'