class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = [i for i in l if i.strip()]
        # print(l)
        return ' '.join(l[::-1])