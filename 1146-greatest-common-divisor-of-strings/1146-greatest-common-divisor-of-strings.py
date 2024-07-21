class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # s1 = set(str1)
        # s2 = set(str2)
        # s3 = s1 - (s2-s1)
        # return ''.join(list(s3))
        n,m=len(str1),len(str2)
        t = min(n,m)

        while n%t!=0 or m%t!=0:
            t-=1
        
        print(t,n,m)
        
        if str1+str2!=str2+str1:
            return ''
        
        return str1[:t] 

        
        