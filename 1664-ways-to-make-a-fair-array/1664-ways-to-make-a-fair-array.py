class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        
        length = len(nums)
        odd= 0
        even = 0 
        
        for index,ele in enumerate(nums):
            
            if index% 2 ==0:
                even+= ele
            else:
                odd+= ele
                
        playing = True
        ans =0
                
        for index,ele in enumerate(nums):
            
            if index==0:
                odd,even = even,odd
                
                
            else:
                
                if (index-1)%2 == 0:
                    even+=nums[index-1]
                    
                else:
                    odd+=nums[index-1]
                    
            if playing:
                odd-=ele
            else:
                even-=ele
                
            playing = not playing 
            
            
            if odd == even:
                ans+=1
        return ans
        