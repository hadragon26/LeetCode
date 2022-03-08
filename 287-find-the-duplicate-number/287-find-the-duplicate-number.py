class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tor = 0 
        har = 0
        
        
        while True:
            tor = nums[tor]
            har = nums[nums[har]]
            if tor ==har:
                break
            
            
        tor = 0
        
        while tor != har:
            tor = nums[tor]
            har = nums[har]
            
        return tor