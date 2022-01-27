class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        if arr[0]>arr[1]:
            return 0
        if arr[-1] > arr[len(arr)-2]:
            return len(arr) -1 
        
        start = 0 
        end = len(arr)-1
        ans = 0
        track = -1
        
        while start <=end:
            mid = (start + end)//2
            
            
                
                
            if arr[mid] > arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid]<arr[mid+1]:
                start = mid +1 
                
            elif arr[mid]< arr[mid-1]:
                end = mid -1 
                
            
            
            
            
            