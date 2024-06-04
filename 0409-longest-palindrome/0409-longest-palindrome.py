class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        t=0
        for i in d:
            if d[i]%2==0:
                t+=d[i]
            else:
                t+=d[i]-1
        if t==len(s):
            return t
        else:
            return t+1

