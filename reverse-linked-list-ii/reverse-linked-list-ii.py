# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """"
        
        if not head:
            return None 
        
        dummy=ListNode(0,head)
        curr = head
        prev = dummy
        
        while left>1:
            prev = curr
            curr = curr.next
            left-=1
            right-=1
            
        prev1 = 0 
        
        
        while right>0:
            
            x = curr.next
            curr.next = prev1
            prev1 = curr
            curr = x
            
            right-=1
            
            
        
        
        prev.next.next =curr
        prev.next = prev1
        return dummy.next"""
        
        
        
        dummy=ListNode(0,head)
        curr = dummy
        index = 0
        
        while curr:
            
            
            if index ==left:
                node = None 
                prev = curr
                while index<=right:
                    nxt = curr.next
                    curr.next = node
                    node = curr
                    curr = nxt
                        
                    index +=1
                if curr == None:
                    start.next =node
                
                    prev.next = curr
                    break
                    
            elif index>right:
                start.next =node
                
                prev.next = curr
                
                break 
                
            else:
                start = curr
                curr = curr.next
                index+=1
                    
            
                    
        return dummy.next
                    
        
        
       
                
                
        
            
            
            