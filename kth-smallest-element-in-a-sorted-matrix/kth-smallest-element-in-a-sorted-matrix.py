class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        res = []
        for lst in matrix:
            for ele in lst:
                if len(res)<k:
                    heappush(res,-ele)
                else:
                    heappushpop(res,-ele)
        
        print(res)
                
        return (-res[0])
                