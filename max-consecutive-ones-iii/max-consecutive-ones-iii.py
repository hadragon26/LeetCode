class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        
        dic = {}
        left = 0 
        count = 0 
        length = 0
        
        for index,num in enumerate(nums):
            
            if num not in dic:
                dic[num]=1
            elif num in dic:
                dic[num]+=1
            if 1 in dic:
                count = max(count,dic[1])
            else:
                count = max(count,0)
                
            while index-left + 1 -count >k:
                
                dic[nums[left]]-=1
                left+=1
                
            length = max(length,index-left+1)
        
        
        return length
                
            
                
            
            