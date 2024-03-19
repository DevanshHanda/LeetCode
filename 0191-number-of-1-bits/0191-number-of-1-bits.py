class Solution:
    def hammingWeight(self, n: int) -> int:
        # converting a bin string n to int c
        c = str("{0:b}".format(n))
        
        return c.count('1')
        