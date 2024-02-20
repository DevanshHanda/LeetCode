class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int max=0;
        int t = 0;
        int index = n;
        for(int i=0;i<n;i++){
            // System.out.println(nums[0]+" "+nums[1]+" "+nums[2]+" "+nums[3]+" "+nums[4]+" "+nums[5]+" "+nums[6]);
            for(int j=0;j<n-i;j++){
                if (max<=(int) Math.abs(nums[j])){
                    max = (int) Math.abs(nums[j]);
                    index = j;
                }
            }
            t = nums[n-i-1];
            nums[index]=t;
            nums[n-i-1]=(int) Math.pow(max,2);
            int y = n-i-1;
            max=0;
        }
    // nums[0]=nums[0]*nums[0];
    return nums;}
}