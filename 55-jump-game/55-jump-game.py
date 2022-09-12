class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        length = len(nums)
        if length ==1:
            return True
        track = 1
        
        for index in range(length-2,-1,-1):
            if index == 0:
                return nums[index]>=track
            if nums[index]<track:
                track+=1
            else:
                track = 1
            
            
            
            
            
        
        
        
        
        
        
        
        
        