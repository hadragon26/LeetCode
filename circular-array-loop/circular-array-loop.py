class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n = len(nums)
        visited = [False]*n
        
        if n ==1:
            return False 
        
        def getNext(index):
            return (index+nums[index])%n
        
        
        
        def isCycle(index):
            
            nxt = getNext(index)
            visited[index] =True
            
            if nxt == index:
                return False
            
            while index!=nxt:
                visited[nxt] =True
                if nums[nxt]*nums[index]<0:
                    return False
                nxt = getNext(nxt)
            
            return True
        
        
        
        for i in range(n):
            if visited[i]:
                continue
            slow = i
            fast = i
            
            while not visited[slow]:
                visited[slow] = True
                fast = getNext(getNext(fast))
                slow = getNext(slow)
                
                if fast == slow and isCycle(slow):
                    return True
        return False
    
    
      
        
                
                
        
            