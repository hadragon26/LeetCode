class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        stack = []
        
        
        
        for num in nums:
            if not stack:
                stack.append(num)
                
            elif num in stack:
                continue
            
            elif num>stack[-1]:
                stack.append(num)
                
                
            else:
                
                l = 0 
                r = len(stack)-1
                
                while r>l:
                    
                    mid = l +(r-l)//2
                    
                    if num >stack[mid]:
                        l = mid +1
                        
                    else:
                        r = mid
                        
                stack[r] = num
                
                
        return len(stack)
        
                
                
            
            