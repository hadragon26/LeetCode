class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0 
        r = 0 
        steps = 0
        farthest = 0
        
        while r<len(nums)-1:
            
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
                
            l =r+1
            r = farthest
            steps+=1
            
        return steps
        
        
        