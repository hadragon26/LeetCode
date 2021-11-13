class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        
        ans = [0 for i in range(len(temperatures))]
        
        
        for index,elem in enumerate(temperatures):
            
            while stack and stack[-1][-1] < elem:
                x,y = stack.pop()
                
                ans[x] = index -x
                
                
            stack.append((index,elem))
            
            
        return ans