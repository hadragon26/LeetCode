class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        
        half = len(nums)//2
        
        
        
        if len(nums) % 2 == 0:
            nums[::2],nums[1::2]= nums[:half][::-1] , nums[half:][::-1]
        else:
            nums[::2],nums[1::2]= nums[:half+1][::-1] , nums[half+1:][::-1]

            
        