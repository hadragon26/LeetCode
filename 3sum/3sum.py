class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        lst = set()
        nums.sort()
        
        for i in range(len(nums)):
            
            l = i+1
            r= len(nums)-1
            
            while l<r:
                if nums[l] + nums[r] > -nums[i]:
                    r-=1
                    
                elif nums[l] + nums[r] < -nums[i]:
                    l+=1
                
                else:
                    lst.add((nums[i],nums[l],nums[r]))
                    print("hi")
                    
                    r-=1
                    l+=1
                    
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                        
        return list(lst)
            
                    
                