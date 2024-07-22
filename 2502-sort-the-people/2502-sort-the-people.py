class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
       t = [[names[i],heights[i]] for i in range(len(heights))]
       t.sort(key=lambda x:x[1], reverse=True)
    #    print(t)
       return [i for i,j in t]
