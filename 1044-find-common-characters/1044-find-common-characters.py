class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = [set([*i]) for i in words]
        c = [Counter(i) for i in words]
        
        t1 = s[0]
        for i in s:
            t1 = t1 & i
        # print(t1)
        t1 = list(t1)
        ma={t1[i]:len(words[0]) for i in range(len(t1))}
        for i in t1:
            for j in c:
                if j[i]<ma[i]:
                    ma[i]=j[i]
        tf = []
        for i in ma:
            tf+=[i]*ma[i]
        return tf
            

