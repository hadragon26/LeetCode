class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        p = [i for i in range(len(s))]
        
        def union(x,y):
            
            px = find(x)
            py = find(y)
            
            if px != py:
                p[py] = px
                
                
        def find(x):
            
            if x!= p[x]:
                p[x] = find(p[x])
            
            return p[x]
        for i in pairs:
            union(i[0],i[1])
            
            
        dic = {}
        ans = list(s)
            
        for idx,ele in enumerate(p):
            if find(ele) not in dic:
                dic[find(ele)] = [idx]
            else:
                dic[find(ele)].append(idx)
                
                
        for i in dic:
            val = dic[i]
            chaar = [s[i] for i in val]
            chaar.sort()
            
            for idx,char in zip(val,chaar):
                ans[idx] = char
                
                
        return "".join(ans)
                
            
        
        
        
            
        
        
        
        
        