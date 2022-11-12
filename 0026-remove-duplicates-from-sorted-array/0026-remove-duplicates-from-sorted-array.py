class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        check,go = 1,1
        
        while go<len(nums):
            if nums[go] not in nums[:check]:
               
                
            
                nums[check]=nums[go]
                
                check+=1
            go+=1
        return check
                
            
            