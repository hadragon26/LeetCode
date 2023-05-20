class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = -1 
    
        for index in range(len(nums)):
            if nums[index]>=0:
                r = index
                
                break
        l = index-1
        ans =[]
        if r <0:
            
            l = len(nums)-1
            while l>=0 :
                ans.append(nums[l]**2)
                l-=1 
            return ans
        
            
            
            

        
        count = 0
        while count < len(nums):
            if l >=0 and r <len(nums):
                if abs(nums[r]) < abs(nums[l]):
                    ans.append(nums[r]**2)
                    r+=1 
                else:
                    ans.append(nums[l]**2)
                    l-=1 
                
            elif l<=0 and r<len(nums):
                 
                ans.append(nums[r]**2)
                r+=1 
            elif r == len(nums) and l>=0:

                ans.append(nums[l]**2)
                l-=1 
            count+=1
        return ans
            
            
        
        
        