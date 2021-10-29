# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head 
        slow = head
        if not head:
            return None
        
        while True:
            slow = slow.next
            
            if not fast or not fast.next:
                return None 
                
            fast =fast.next.next
            
            if fast == slow:
                break
                
        
        
        while fast != head:
            fast = fast.next
            head = head.next
            
        return fast
            
            
            
                
                
    
                    
                
            