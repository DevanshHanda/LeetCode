# class Solution:
#     def minimumLength(self, s: str) -> int:
#         l = []
#         t = s[0]
#         k=s[1:]
#         for i in k:
#             if t[-1]!=i:
#                 l.append(t)
#                 t=''
#             t+=i
#         l+=[t]
#         i,j=0,len(l)-1
#         while i<j:
#             if l[i][0]==l[j][0]:
#                 l[i] = ''
#                 l[j] = ''
#                 j-=1
#                 i+=1
#             if l[i][0]!=l[j][0]:
#                 q = ''.join(l)
#                 return len(q)
#         print(l[i])
#         if len(l[i])==1:
#             return 1
#         else:
#             return 0
#         print(l)
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            char = s[l]
            l += 1
            r -= 1
            while l <= r and s[l] == char:
                l += 1
            while l <= r and s[r] == char:
                r -= 1
        
        return r - l + 1