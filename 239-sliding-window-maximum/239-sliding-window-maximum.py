class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        
        
        track = deque()
        result = []
        l,r = 0,0 
        
        
        while r< len(nums):
            
            
            
            while track and nums[track[-1]]<=nums[r]:
                track.pop()
                
            track.append(r)
            
            
            if l > track[0]:
                track.popleft()
                
                
            if r-l+1>=k:
                result.append(nums[track[0]])
                l+=1
            
            
            r+=1
        return result
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            