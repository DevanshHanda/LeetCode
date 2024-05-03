class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        for i in d:
            d[i] = [j for j in d[i]]
        print(d)

        def mult(a,b):
            c=[]
            for i in a:
                for j in b:
                    c.append(i+j)
            return c
        if len(digits)==0:
            return []
        if len(digits)==1:
            return d[digits]
        
        a = d[digits[0]]
        for i in digits[1:]:
            a = mult(a,d[i])
        return a

