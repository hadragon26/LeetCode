class Solution:

    def __init__(self, nums: List[int]):
        self.default = nums
        
        
        
        
        
        
        

    def reset(self) -> List[int]:
        return self.default
        

    def shuffle(self) -> List[int]:
        nums = self.default[:]
        
        for i in range(len(nums)):
            
            ran = randrange(i,len(nums))
            nums[i],nums[ran] = nums[ran],nums[i]
            
        return nums
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()