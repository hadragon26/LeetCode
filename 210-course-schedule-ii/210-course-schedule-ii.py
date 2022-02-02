class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        from collections import deque as q
        
        
        inDeg = {i:0 for i in range(numCourses)}
        
        vert = {i:[] for i in range(numCourses)}
        
        
        for lst in prerequisites:
            
            child, parent = lst 
            
            inDeg[child] += 1 
            
            vert[parent].append(child)
            
            
        ans = q()
        check = []
        
        
        for i in inDeg:
            
            if inDeg[i] == 0:
                ans.append(i)
            
        while ans:
            tex = ans.popleft()
            check.append(tex)
            
            
            for d in vert[tex]:
                inDeg[d]-=1
                
                if inDeg[d] == 0:
                    
                    ans.append(d)
                    
        if len(check) != numCourses:
            return []
        return check
        
        
        
        