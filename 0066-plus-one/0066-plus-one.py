class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = ''.join([str(x) for x in digits])
        t = str(int(t)+1)
        return [int(x) for x in t]
        