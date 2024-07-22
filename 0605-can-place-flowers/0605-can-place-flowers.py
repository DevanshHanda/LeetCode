class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if n==0:
            return True
        if len(flowerbed)<3:
            if n>1:
                return False
            elif 1 in flowerbed:
                return False
            else:
                return True

        # if len(flowerbed)==3:




        for i in range(0,len(flowerbed)-2):
            # print('hiji')

            # print(flowerbed)
            if i==0 :
                # print(flowerbed[i:i+3])
                if (flowerbed[i:i+3]==[0]*2+[1]):
                    flowerbed[0]=1
                    c+=1
                elif flowerbed[i:i+3]==[0]*3:
                    flowerbed[0]=1
                    flowerbed[2]=1
                    c+=2


            elif i==len(flowerbed)-3 and (flowerbed[i:i+3]==[1]+[0]*2):
                c+=1
                flowerbed[-1]=1

            elif flowerbed[i:i+3]==[0]*3 :
                flowerbed[i+1]=1
                c+=1
            
            if i==len(flowerbed)-3 and flowerbed[len(flowerbed)-2:]==[0]*2:
                flowerbed[-1]=1
                c+=1

            if c>=n:
                return True
            # print(flowerbed[i:i+3])
            # print(flowerbed,c)

        return False
