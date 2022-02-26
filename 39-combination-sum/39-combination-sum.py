class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(curr,lst,total):
            
            if total == target:
                ans.append(lst.copy())
                return
            
            if curr>=len(candidates) or total >target:
                return
    
            lst.append(candidates[curr])
            
            dfs(curr,lst,total+candidates[curr])
            lst.pop()
            dfs(curr+1,lst,total)
            
        dfs(0,[],0)
        
        return ans
                