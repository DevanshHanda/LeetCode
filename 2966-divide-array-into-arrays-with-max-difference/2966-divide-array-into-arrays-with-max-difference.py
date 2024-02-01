class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=k
        k = sorted(nums)
        l=[]
        if len(k)%3!=0:
            return []
        j=0
        print(sorted([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]))
        l1=[0]*3
        prev=k[0]
        for i in k:
            l1[j]=i
            if j==2:
                if l1[2]-l1[0]>n:
                    return []
                l.append(l1)
                l1=[0]*3
                # prev=i
            if j==0:
                prev=i
            if i-prev>n:
                return []
            prev = i
            j=(j+1)%3
        return l