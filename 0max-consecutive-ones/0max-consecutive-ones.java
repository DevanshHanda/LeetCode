class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count=0;
        int max =0;
        for(int i=0;i<nums.length;i++){
            System.out.println(nums[i]);
            if(nums[i]==1){
                count+=1;
                
            }
            else if(nums[i]==0){
                if(max<count){
                    max = count;
                }
                count=0;
            }
        }
        if(max<count){
                    max = count;
                }
    return max;
    }
}