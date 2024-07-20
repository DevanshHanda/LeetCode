class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # # l = [k for k in intervals]
        # d = [b for a,b in intervals]
        # l = sorted(list(set(d)))
        # k=[]
        # # print(l)
        # for i in l:
        #     for a,b in intervals:
        #         if b==i:
        #             k.append([a,b])

        # better sorting

        intervals.sort(key=lambda x: x[1])
        k = intervals[:]

        # print()
        # print(k)
        prev,count=k[0][1],1
        for i in range(1,len(k)):
            # print(prev)
            if k[i][0]>=prev:
                # print(k[i])
                prev = k[i][1]
                count+=1
            
        return len(intervals)-count
        
