class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        arr = nums
        l=0
        r= len(arr)-1
        x = target
        while l <= r:
            mid = l + (r - l) // 2
 
            # Check if x is present at mid
            if arr[mid] == x:
                return mid
 
            # If x is greater, ignore left half
            elif arr[mid] < x:
                l = mid + 1
 
        # If x is smaller, ignore right half
            else:
                r = mid - 1
        # binarySearch(arr, 0, len(arr)-1, x)
    # If we reach here, then the element
    # was not present
        return l