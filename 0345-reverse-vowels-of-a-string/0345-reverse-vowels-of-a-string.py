class Solution:
    def reverseVowels(self, s: str) -> str:
        sa = set(['a','e','i','o','u','A','E','I','O','U'])
        s=[i for i in s]
        i,j=0,len(s)-1
        while i<j:
            if s[i]not in sa:
                i+=1
            if s[j] not in sa:
                j-=1
            if (s[i] in sa) and (s[j] in sa):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            
        return ''.join(s)
        