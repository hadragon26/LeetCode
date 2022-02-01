class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            
        
        
        
        nums.sort()
        print(nums)
        su  =sum(nums) // 2 
        
        if sum(nums) % 2 != 0:
            return False 
        
        lst  = [[False for i in range(su+1)]for i in range(len(nums)+1)]
        
        
        for i in range(len(lst)):
            if i==0:
                    continue 
            if nums[i-1]>(len(lst[0])):
                break
            if nums[i-1] < len(lst[0]):
                lst[i][nums[i-1]] = True
                
                
             
            for j in range(len(lst[0])):
                if j<nums[i-1] :
                
                    lst[i][j] = lst[i-1][j]  
                elif j>nums[i-1]:
                     lst[i][j] = lst[i-1][j] or lst[i-1][j-nums[i-1]]
                    
                
                    
        
        return lst[-1][-1]          
                    
                        
                    
        
        
        
        