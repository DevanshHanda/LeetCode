class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        o=''
        n = min(len(word1),len(word2))

        # for i in range(n):
        #     o+=word1[i]+word2[i]
        # return o

        while i<len(word1) or j<len(word2):
            if i<len(word1):
                a = word1[i]
                i+=1
            else:
                a=''
            if j<len(word2):
                b = word2[j]
                j+=1
            else:
                b=''

            o+=a+b
        return o


        