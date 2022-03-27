class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.index = 0
        self.track = {}

    def insert(self, val: int) -> bool:
        
        if val not in self.track:
            self.dic[self.index] = val
            self.track[val] = self.index
            self.index+=1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        
        if val not in self.track or self.index == 0:
            return False
        
        index = self.track[val]
        x = self.dic[self.index-1]
        self.dic[self.index-1] = val
        self.dic[index] = x
        del self.dic[self.index-1]
        self.track[x] = index
        del self.track[val]
        
        self.index-=1
        
        
        return True

    def getRandom(self) -> int:
        
        ran = randint(0,self.index-1)
        
        return self.dic[ran]
        
        
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()