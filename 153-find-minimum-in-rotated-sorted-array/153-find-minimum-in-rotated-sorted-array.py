class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        #binary search 
        
        l =0 
        r = len(nums) - 1 
        
        if r == 0:
            return nums[0]
        
        if nums[l]<= nums[r]:
            return nums[l]
        
        while l<=r :
            
            mid = (l+r)//2
            
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]> nums[mid]:
                return nums[mid]
            
            
            if nums[mid] >=nums[l]:
                l = mid+1 
                
            else:
                r = mid -1 
            
            