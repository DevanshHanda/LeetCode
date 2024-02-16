class Solution:
    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    #     count = {key : arr.count(key) for key in arr}
    #     l = sorted(list(count.values()))
    #     for i in range(len(l)):
    #         k-=l[i]
    #         if k==0:
    #             return len(l)-i-1
    #         if k<0:
    #             return len(l)-i
    #     return 0
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in sorted(cnt): 
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt.pop(key)
            else:
                return remaining - k // key
        return remaining
