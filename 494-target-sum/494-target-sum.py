class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        su  = sum(nums)
        if target>su or target<-su:
            return 0
        
        
        lst = [[0 for i in range(su*2+1)] for i in range(len(nums)) ]
        
        
            
        
        lst[0][abs(nums[0]+su)] += 1
        lst[0][abs(nums[0]-su)] += 1
        
        
        
        
        for i in range(1,len(nums)):
            
            for j in range(su*2+1):
                
                if j-nums[i] >= 0:
                    lst[i][j] += lst[i-1][j-nums[i]]
                if j+nums[i] < su*2+1 :
                    lst[i][j] += lst[i-1][j+nums[i]]
        
        return(lst[-1][su+target])