class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        
        dic = {1:0,2:1}
        q = []
        
        
        def dfs(nu):
            
            if nu in dic:
                return dic[nu]
            
            
            if nu %2 == 0:
                
                dic[nu] = dfs(nu//2)+1
                return dic[nu]
                
                
            elif nu%2 != 0:
                dic[nu] = dfs((3*nu)+1)+1
                return dic[nu]
                
            
                
            
        dfs(7)
        #print(dic)
        
        
        for i in range(lo,hi+1):
            dfs(i)
            heappush(q,(dic[i],i))
                     
                     
        c= 1
        #print(dic)
                     
        while c<k:
            heappop(q)
            c+=1
                     
        return heappop(q)[1]
                     

            
                
                
        