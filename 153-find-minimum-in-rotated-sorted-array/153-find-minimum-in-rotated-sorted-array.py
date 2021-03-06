class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        start = 0 
        
        end = len(nums)-1 
        
        while end > start:
            
            
            mid = start + (end-start) //2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] > nums[end]:
                start = mid +1 
                
            else:
                end = mid 
                
                
        return nums[start]