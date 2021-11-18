class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        lst = [] 
        
        nums.sort()
        
        
        for i in range(len(nums)-3):
            if i!=0 and nums[i-1] == nums[i]:
                continue
            
            
            for j in range(i+1,len(nums)-2):
                if j!=i+1 and nums[j-1] == nums[j]:
                    continue 
                    
                l = j+1
                r=len(nums)-1
                
                while l<r:
                    
                    if nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r-=1
                    
                    elif nums[i] + nums[j] + nums[l] + nums[r] <target:
                        l+=1
                        
                    else:
                        lst.append([nums[i],nums[j],nums[l],nums[r]])
                        r-=1
                        l+=1
                        
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                            
                            
        return lst
                    