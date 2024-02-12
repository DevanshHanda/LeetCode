class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        window=len(str(low))
        l='123456789'
        i=0
        a=[]
        c=int(l[i:window+i])
        while c<low:
            i+=1
            if window+i-1==9:
                i=0
                window+=1
                if window==10:
                    return []
            c=int(l[i:window+i])
        while c<=high:
            a.append(c)
            i+=1
            if window+i-1==9:
                i=0
                window+=1
                if window==10:
                    break

            c=int(l[i:window+i])
        return a
            




            
            

