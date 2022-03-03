class Node:
    def __init__(self,key,value):
        self.key,self.value = key,value
        self.prev,self.next = None,None






class LRUCache:
    
    from collections import deque

    def __init__(self, capacity: int):
        self.dic ={}
        self.limit  = capacity
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self,Node):
        prev,nxt = Node.prev,Node.next
        prev.next,nxt.prev = nxt,prev
        
    
    def insert(self,Node):
        
        prev,nxt = self.right.prev,self.right
        
        prev.next,nxt.prev = Node,Node
        Node.prev = prev
        Node.next = nxt
        

    def get(self, key: int) -> int:
        #print(self.dic)
        
        if key in self.dic:
            self.remove(self.dic[key])
        
        
            self.insert(self.dic[key])
                
            
            
        
            return self.dic[key].value
        return -1
    
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            self.remove(self.dic[key])
            
            
        self.dic[key] = Node(key,value)
        self.insert(self.dic[key])
        
        if len(self.dic) >self.limit:
            least = self.left.next
            del self.dic[least.key]
            self.remove(least)
            
            
            
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)