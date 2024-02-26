class Solution:
    def isValid(self, s: str) -> bool:
        stack=[0]
        p = [')',']','}']
        for i in s:
            if i in p:
                if stack[-1]==0:
                    return False
                t=stack.pop()
                if t=='(' and i!=')':
                    return False
                elif t=='{' and i!='}':
                    return False
                elif t=='[' and i!=']':
                    return False
            else:
                stack.append(i)
        if stack[-1]==0:
            return True
        else:
            return False