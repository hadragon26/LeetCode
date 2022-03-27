class Trie:

    def __init__(self):
        self.dic = {}
        self.dic1 ={}

    def insert(self, word: str) -> None:
        self.dic[word] =1
        temp = ''
        
        for i in word:
            temp+=i
            if temp not in self.dic1:
                self.dic1[temp] = 1 
            
        
        

    def search(self, word: str) -> bool:
        if word in self.dic:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.dic1:
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)