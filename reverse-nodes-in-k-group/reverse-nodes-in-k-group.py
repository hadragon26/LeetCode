# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #find the length 
        
        dummy = ListNode(0,head)
         
        prev = dummy
        
        def find(curr,k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr 
        
        while True:
            
            kth = find(prev,k)
            if not kth:
                break
            
            latter = kth.next
                
            
            curr = prev.next
            after = latter 
            
            while curr!=latter:
                nxt = curr.next
                curr.next= after 
                after = curr
                curr = nxt
                
            temp = prev.next 
            prev.next = kth
            prev = temp
            
            
        return dummy.next
            
            
                
            
            
            
            
            
        
            
            
            
            
        