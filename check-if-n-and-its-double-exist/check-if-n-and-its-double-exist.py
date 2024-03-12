class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0)>=2:
            return True
        if 0 in arr:
            arr.remove(0)
        for i in arr:            
            if 2*i in arr:
                return True
        return False