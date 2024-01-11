class Solution:
    def removeStars(self, s: str) -> str:
        l=[]
        for i in s:
            # print(i)
            if i=='*':
                l.pop()
                # print('---*')
            else:
                l.append(i)
                # print(i)
        # print(l)
        return ''.join(l)