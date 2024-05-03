class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = [int(i) for i in version1.split('.')]
        l2 = [int(i) for i in version2.split('.')]

        i=0
        while i<len(l1) and i<len(l2):
            if l1[i]>l2[i]:
                return 1
            elif l1[i]<l2[i]:
                return -1
            i+=1
        if i==len(l1) and i==len(l2):
            return 0
        if i==len(l1):
            if max(l2[i:])!=0:
                return -1
            else:
                return 0
        if i==len(l2):
            if max(l1[i:])!=0:
                return 1
            else:
                return 0
        




        
        
