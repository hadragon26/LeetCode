class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        dic= {}
        ans = []
        index = 0 
        for i in strs:
            key = "".join(sorted(i))
            
            if key in dic:
                ans[dic[key]].append(i)
                
            else:
                dic[key] = index
                ans.append([i])
                index+=1
                
        return ans
                
            