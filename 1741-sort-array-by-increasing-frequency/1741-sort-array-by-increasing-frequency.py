from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        da={}
        for i in d:
            if d[i] not in da:
                da[d[i]]=[i]
            else:
                da[d[i]].append(i)
        
        for i in da:
            da[i].sort(reverse = True)
        



        l = [[i,da[i]] for i in da]

        l.sort(key = lambda x:x[0])
        t = []
        for i in l:
            for j in i[1]:
                t+=[j]*i[0]
        print(t)
        return t