# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head
        if not head.next.next:
            return head
            
        
        n=1
        curr =head
        
        while curr.next.next:
            
            
            
            
                
            x =curr.next
            
            curr.next = curr.next.next
            
                
            if n ==1:
                even = x
                
            if n%2 ==1:
                prev = curr.next
                
            curr = x
            
            n+=1 
        
        #print(prev)
        #print(even)
        curr.next = None
        prev.next = even
        return head
            
            
            
        
        
            
           
        
        
            
            
        