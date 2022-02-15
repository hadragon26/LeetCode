class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        
        index = 0 
        
        
        while index<len(nums):
            
            if index + 1 == nums[index]:
                index+=1
                
            elif nums[index] <= 0:
                index+=1
            elif nums[index] >len(nums):
                index+=1
                
            elif nums[index] == nums[nums[index]-1]:
                index += 1
           
                
            else:
                
                b = nums[index]-1
                a = index
                
                
                nums[a],nums[b] = nums[b],nums[a]
                
                
                
                
                
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
            
            
        else:
            return len(nums)+1
            
            
            
            
            
        
        
        
        