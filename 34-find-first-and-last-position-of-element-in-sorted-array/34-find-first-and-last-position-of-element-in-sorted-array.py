class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        
        
        
        
        while end>= start:
            
            mid = (start+end)//2
            
            if nums[mid] == target:
                f = mid 
                l = mid 
                
                while mid >0 and nums[mid-1]==nums[mid]:
                    f-=1
                    mid = f 
                    
                mid = l
                    
                while mid+1 <= end and nums[mid+1] == nums[mid]:
                    l+=1 
                    mid = l
                    
                return [f,l]
            
            elif nums[mid]< target:
                start = mid + 1
                
            elif nums[mid] > target:
                end -=1
                
                
        return [-1,-1]
                    
                    
                    
                
            
        
            
            
            
            