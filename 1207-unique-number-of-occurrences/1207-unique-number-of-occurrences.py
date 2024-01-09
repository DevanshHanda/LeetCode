class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = dict()
        l=[]
        for i in arr:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for i in a:
            l.append(a[i])
        n=len(l)
        s=set(l)
        m=len(s)
        if n==m:
            return True
        else:
            return False