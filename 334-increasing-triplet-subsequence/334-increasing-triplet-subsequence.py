class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        check = True
        ma = float('inf')
        mi = float('inf')
        i =0 
        
        while i < len(nums):
            mi = min(mi,nums[i])
            
                
            if nums[i] > mi:
                
                ma = min(ma,nums[i])
                        
           
            if  nums[i]> ma:
                return True
            
            
                
                
            i+=1
            
        return False
                
                        
            