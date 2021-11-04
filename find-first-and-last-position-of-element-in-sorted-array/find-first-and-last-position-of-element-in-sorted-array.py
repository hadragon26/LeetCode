class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        ans = [-1,-1]
        
        
        
        def bin(start,end,playing):
            
            key = -1
            
            while end>= start:
                mid = (start +end) //2
                
                
                if target < nums[mid]:
                    end = mid -1 
                
                elif target > nums[mid]:
                    start = mid+1
                    
                else:
                    key = mid
                    
                    if playing:
                        end = mid -1 
                        
                    else:
                        start = mid +1
                        
            return key 
        
        ans[0] = bin(start,end,True)
        if ans[0]!= -1:
            ans[-1]= bin(start,end,False)
        
        
        return(ans)
                        
                    
                
            
        
            
            
            
            