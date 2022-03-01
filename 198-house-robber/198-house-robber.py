class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        track = [0 for i in range(len(nums))]
        
        for index,ele in enumerate(nums):
            if index-2 >=0:
                track[index] = max(ele + track[index-2],track[index-1])
                
            elif index == 0:
                track[index] = ele
                
            elif index == 1:
                track[index]= max(ele,track[index-1])
                
                
        return track[-1]
                
                
                