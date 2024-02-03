class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=str(x)
        l=[*k]
        ls=l.copy()
        l.reverse()
        # print(l,ls)
        for i in range(len(l)):
            print(l[i],ls[i])
            if l[i]!=ls[i]:
                return False
        return True




