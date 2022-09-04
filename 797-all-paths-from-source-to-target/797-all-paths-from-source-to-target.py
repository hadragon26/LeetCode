class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        q = [[0]]
        
        target = len(graph) -1 
        result = []
        while q:
            ele = q.pop(0)
            
            if ele[-1] == target:
                result.append(ele)
                
            for neigh in graph[ele[-1]]:
                q.append(ele+[neigh])
                
        return result