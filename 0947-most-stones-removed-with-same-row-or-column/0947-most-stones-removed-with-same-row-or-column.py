class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import deque
        def check(coor,coor1):
            
            if coor1[1]==coor[1] or coor1[0] == coor[0]:
                    
                return True
            return False
        
        q = deque()
        visited = [False for i in range(len(stones))]
        
        
        ans = 0
        for index , coor in enumerate(stones):
            if visited[index] == False:
                q.append(coor)
                visited[index] = True
                count = 0
                while q:
                    x,y = q.popleft()
                    count+=1
                    for index1,coor1 in enumerate(stones):
                        if check((x,y),coor1) and visited[index1] == False:
                            q.append(coor1)
                            visited[index1] = True
                            
                ans += count -1
                
        return ans
                            
                
        
        
        
        
                            
                            
                            
                            
                        
                
    
            
            
            