class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            String temp = ""+nums[i];
            int n = String.valueOf(temp).length();
            if(n%2==0){
                count+=1;
            }
        }
    return count;}
}