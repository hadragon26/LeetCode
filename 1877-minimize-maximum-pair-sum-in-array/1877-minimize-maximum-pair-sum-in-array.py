class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        
        nums.sort()
        
        l = 0 
        r = len(nums)-1
        
        ma = 0
        
        while l<r:
            
            sa= nums[l]+nums[r]
            if sa>ma:
                ma = sa
                
            l+=1
            r-=1
                
        return ma