class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # n=len(needle)
        # if needle==haystack:
        #     return 0
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:i+n] == needle:
        #         return i
        # return -1

        # both are correct
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1