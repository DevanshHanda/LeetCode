class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        # print(citations)
        for i,v in enumerate(citations):
            # print(v)
            if n - i <= v:
                return n - i
        return 0