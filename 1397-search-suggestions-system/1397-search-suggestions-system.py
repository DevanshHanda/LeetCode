class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        p=list()
        for i in range(1,len(searchWord)+1):
            p.append(sorted([k for k in products if i<=len(k) and (searchWord[:i] in k[:i])])[:3])
        return p