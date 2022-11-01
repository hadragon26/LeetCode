class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        track = [float('-inf') for i in range(len(nums))]
        ans = float('-inf')
        
        for index,num in enumerate(nums):
            
            if index == 0:
                
                track[index] = num
            else:
                
                track[index] = max(num,num+track[index-1])
                
            ans = max(track[index],ans)
                
        return ans
            
            
            
        
        
        
        