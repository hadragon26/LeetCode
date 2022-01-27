class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        #find the maximum
        
        
        start = 0 
        end = len(nums)-1
        
        
        #find the smallest index
        
        while end>start:
            
            mid = start + (end-start)//2
            
            if nums[mid] > nums[end]:
                start = mid +1
                
            else:
                end = mid 
                
        pivot = start 
        
        start = 0
        end = len(nums) -1 
        
        
        if target >= nums[pivot] and target<=nums[end]:
            start = pivot
            
        else:
            end = pivot - 1
        while end>=start:
            
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                
                end = mid -1
                
            elif nums[mid] < target:
                start = mid +1
                
        return -1
            
        
            
        
        
        