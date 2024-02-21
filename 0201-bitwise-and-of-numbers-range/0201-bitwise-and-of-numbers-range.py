class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # s = right
        # if s!=0:
        #     p=(int(log(s,2)))
        #     c=2**p
        #     if c<left:
        #         s=left
        #         for i in range(left+1,right+1):
        #             s=s&i
        #         return s
        #     return c&left

        # return s 
        while left < right:
            
            right = right & (right-1)
      
        return left & right
          
        