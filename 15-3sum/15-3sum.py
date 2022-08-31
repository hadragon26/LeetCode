class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()
        print(nums)
        
        
        end = len(nums)-1 
        
        start = 0 
        lst = set()
        count = 0
        while end > start:
            t=start+1
            
            
            
            while end > t:
            
                if nums[end]+nums[t]+nums[start] == 0 :
                    lst.add((nums[start],nums[t],nums[end]))
                    
                    end -=1
                        
                    
                    
                    
                    
                    
                    
                    
                
                elif nums[end]+nums[t]+nums[start] > 0:
                    end -=1
                else :
                    
                    
                    t+=1 
                
                        
                
            start += 1 
            end = len(nums)-1
        
             
            
            
        return lst
        
            
                    
                