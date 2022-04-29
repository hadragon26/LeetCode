class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return 0 
        
        
        su = 0 
        streak = 0 
        d= nums[1]-nums[0]
        
        
        for i in range(2,len(nums)):
            
            if nums[i]-nums[i-1]==d:
                streak+=1 
                su+= streak
            else:
                d= nums[i]-nums[i-1]
                streak = 0
                
                
        return su
            
            
            
            
                