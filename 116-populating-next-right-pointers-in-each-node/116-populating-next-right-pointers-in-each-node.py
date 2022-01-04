"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque as queue
        
        
        if not root:
            return None
        
        q = queue()
        q.append([root])
        playing = True
        
        while q:
            node = q.popleft()
            lst =[]
            length = len(node)
            
            for index,ele in enumerate(node):
                if not ele.left or not ele.right:
                    playing = False
                    break
                if length == 1:
                    
                    lst.append(ele.left)
                    ele.left.next = ele.right
                    lst.append(ele.right)
                    
                else:
                    
                    lst.append(ele.left)
                    ele.left.next = ele.right
                    lst.append(ele.right)
                    if index+1 < length:
                        ele.right.next = node[index+1].left
            if playing == False:
                break
            q.append(lst)
        return root
            
                    
                    

                
                
        
        
       
        
    
    
    