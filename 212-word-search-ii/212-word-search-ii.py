class Trie:
    def __init__(self):
        self.children = {}
        self.isFinal = False
    def add(self,word):
        cur =self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.isFinal =True
    def prune(self,word):
        curr = self
        stack = []
        for ch in word:
            stack.append(curr)
            curr = curr.children[ch]
        curr.is_word = False

        for t_node, ch in reversed(list(zip(stack, word))):
            if len(t_node.children[ch].children) > 0:  # has children
                return
            else:
                del t_node.children[ch]
                
            
                
        



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        root =Trie()
        
        track = set()
        ans = set()
        
        for word in words:
            root.add(word)
               
        col = len(board[0])
        row = len(board)
            
        
        def dfs(x,y,word,node):
            
            
            
            
                
            if x<0 or x>=row or y<0 or y>=col or board[x][y] not in node.children or (x,y) in track:
                return 
            
            
           
                
                
            
            track.add((x,y))
            
            node = node.children[board[x][y]]
            word = word+board[x][y]
            if node.isFinal:
                ans.add(word)
                root.prune(word)
            
            
            dfs(x+1,y,word,node) 
            dfs(x-1,y,word,node ) 
            dfs(x,y-1,word,node )  
            dfs(x,y+1,word,node )
            
            
            track.remove((x,y))
            
        
        
        for x in range(row):
            for y in range(col):
                dfs(x,y,'',root)
                
                
        return ans
            
            
        
            
            
                
        