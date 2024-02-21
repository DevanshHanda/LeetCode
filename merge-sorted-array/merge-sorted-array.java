class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // System.out.println(nums1.length);
        // System.out.println(nums2.length);
        // m = nums1.length;
        // n = nums2.length;
        for(int i=0;i<n;i++){
            // System.out.println(i);
            nums1[m+i]=nums2[i];
        }
        // if(m>=n){
        //     for(int i=0;i<n;i++){
        //     System.out.println(i);
        //     nums1[n+i]=nums2[i];
        //     }
        // }
        // else{
        //     for(int i=0;i<n;i++){
        //     System.out.println(i);
        //     nums1[n+i]=nums2[i];
        //     }
        // }
        m = m+n;
        
        int temp = 0;  
         for(int i=0; i < m; i++){  
                 for(int j=1; j < (m-i); j++){  
                          if(nums1[j-1] > nums1[j]){  
                                 //swap elements  
                                 temp = nums1[j-1];  
                                 nums1[j-1] = nums1[j];  
                                 nums1[j] = temp;  
                         }  
                          
                 }  
         }  

    }
}