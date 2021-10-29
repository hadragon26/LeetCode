class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        su = float("inf")
        ans = 0 
        
        for i in range(len(nums)):
            
            l = i+1
            r = len(nums)-1
            
            
            while l<r:
                if abs(target - (nums[l] + nums[r] + nums[i])) < su:
                    su = abs(target - (nums[l] + nums[r] + nums[i]))
                    ans = nums[l] + nums[r] + nums[i]
                    
                    
                    
                if nums[l] + nums[r] < target- nums[i]:
                    l+=1
                elif nums[l] + nums[r] > target- nums[i]:
                    r-=1
                else:
                    return nums[l] + nums[r] + nums[i]
        return ans
                
                    
                