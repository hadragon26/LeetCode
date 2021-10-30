# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head:
            return None 
        
        
        curr = head
        prev = None 
        
        while left>1:
            prev = curr
            curr = curr.next
            left-=1
            right-=1
            
        tail = curr
        conn = prev
        
        print(tail)
        
        print(prev)
        
        while right>0:
            
            x = curr.next
            curr.next = prev
            prev = curr
            curr = x
            
            right-=1
            
            
        
            
        if conn != None:
            conn.next = prev
            
            
            
        else:
            head = prev
            
        tail.next = curr
        return(head)
            
        
        
       
                
                
        
            
            
            