class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        s= 0
        f = 1
       
        
        while f< len(nums):
            x = nums[s]
            
            
            while f<len(nums) and nums[f] == x:
                f+=1 
            if f<len(nums):
                s+=1
                nums[s] = nums[f]
                f+=1
                
            

        
        return s+1
            