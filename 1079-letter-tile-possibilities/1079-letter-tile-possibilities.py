class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        br = set()
        def dfs(tiles,ans):
            
            if not tiles:
                if ans:
                    br.add(ans)
                return 
            else:
                for index,ele in enumerate(tiles):
                    temp = tiles[:index]+tiles[index+1:]
                    dfs(temp,ans+ele)
                    dfs(temp,ans)
                    
        dfs(tiles,"")
        return len(br)
        
            