class Solution:
    def equalFrequency(self, word: str) -> bool:
        s=list(set(word))
        if len(s)==1:
            return True
        if len(s)==len(word):
            return True
        l=[word.count(s[x]) for x in range(len(s)) ]
        m = min(l)
        if l.count(1)==1:
            l.remove(1)
            if len(set(l))==1:
                return True
            else:
                return False
        f=0
        for i in l:
            print(i,m)
            if i-m==1:
                f+=1
        if f==1:
            return True
        else:
            return False
            
