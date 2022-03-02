class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        ans =[]
        
        for i in nums:
            ans.append(str(i))
            
        def compare(s1,s2):
            
            if s1+s2 > s2+s1:
                return -1
            else:
                return 1
            
        
        nums = sorted(ans,key=cmp_to_key(compare))
        
        return str(int(''.join(nums)))
                
            