from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        freq1 = {char:word1.count(char) for char in set(word1)}
        freq2 = {char:word2.count(char) for char in set(word2)}
        return sorted(freq1.keys()) == sorted(freq2.keys()) and sorted(freq1.values()) == sorted(freq2.values())
        
        # v1 = set(word1)==set(word2)
        # d1=dict()
        # d2=dict()
        # for i in word1:
        #     if i not in d1:
        #         d1[i]=1
        #     else:
        #         d1[i]+=1
        # for i in word2:
        #     if i not in d2:
        #         d2[i]=1
        #     else:
        #         d2[i]+=1
        # k1=list(d1.values())
        # k2=list(d2.values())
        # k1.sort()
        # k2.sort()
        # v2=k1==k2
        # print(list(k1),list(k2))
        # return v1 and v2

        # return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())