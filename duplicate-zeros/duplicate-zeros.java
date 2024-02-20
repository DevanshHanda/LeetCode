class Solution {
    public void duplicateZeros(int[] arr) {
        int n = arr.length;
        int[] s = new int[n];
        int i = 0; // s
        int j = 0; // arr
        while(i<n){
            if(arr[j]==0){
                s[i]=0;
                i++;
                if(i>=n){
                    break;
                }
                s[i]=0;
            }
            else{
                s[i]=arr[j];
            }
            j++;
            i++;
            
        }
        for(i=0;i<n;i++){
            arr[i]=s[i];
        }
    }
}