class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       
        su = 0
        r = 0 
        l = 0
        l1 = float("inf")
        
        while r< len(nums):
            
            su += nums[r]
            
            while su>=target:
                l1 = min(r-l+1,l1)
                su -= nums[l]
                l+=1
            r+=1
        
        if l1 == float("inf"):
            return 0
        return l1
                
                
                
                
            
                