class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0 
        lst = []
        
        while i < len(nums):
            
            j = nums[i] -1
            
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j] , nums[i]
            else:
                
                i+=1
            
                
                
        print(nums)
                
        for i, nu in enumerate(nums):
            if nu -1 != i:
                lst.append(i+1)
                
        return lst
                
        
                
                
        