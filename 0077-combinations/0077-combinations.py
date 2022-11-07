class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        track = list(range(1,n+1))
        #rint(track)
        lst = []
        def dfs(track,ans):
            
            if not track:
                if len(ans) == k:
                    lst.append(ans)
                return
            #print(track[1:],ans,track[0])
            if len(ans) == k:
                lst.append(ans)
                return
            x = ans[:]
            
            x.append(track[0])
            
            
            dfs(track[1:],x)
            
            dfs(track[1:],ans)
            
            
        
        dfs(track,[])
        return lst
            