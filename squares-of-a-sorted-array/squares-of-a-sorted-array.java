// class Solution {
//     public int[] sortedSquares(int[] nums) {
//         int n = nums.length;
//         int max=0;
//         int t = 0;
//         int index = n;
//         for(int i=0;i<n;i++){
//             // System.out.println(nums[0]+" "+nums[1]+" "+nums[2]+" "+nums[3]+" "+nums[4]+" "+nums[5]+" "+nums[6]);
//             for(int j=0;j<n-i;j++){
//                 if (max<=(int) Math.abs(nums[j])){
//                     max = (int) Math.abs(nums[j]);
//                     index = j;
//                 }
//             }
//             t = nums[n-i-1];
//             nums[index]=t;
//             nums[n-i-1]=(int) Math.pow(max,2);
//             int y = n-i-1;
//             max=0;
//         }
//     // nums[0]=nums[0]*nums[0];
//     return nums;}
// }

class Solution {
    public int[] sortedSquares(int[] nums) {
        int i=0;
        int j=nums.length-1;
        int[] sq=new int[nums.length];
        int r=sq.length-1;
        while(i<=j){
            if(Math.abs(nums[i])>Math.abs(nums[j])){
                sq[r]=nums[i]*nums[i];
                i++;
                r--;
            }else{
                sq[r]=nums[j]*nums[j];
                j--;
                r--;
            }
        }
        return sq;
    }
}