# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        add = False 
        val = l1.val+l2.val
        if val>=10:
            add = True
        if add:
            ans = ListNode(l1.val+l2.val-10)
        else:
            ans = ListNode(l1.val+l2.val)
        curr = ans    
        l1 = l1.next
        l2 = l2.next
        
        while l1 or l2:
            if l1 and l2:
                if add:
                    val = l1.val+l2.val+1
                else:
                    val = l1.val+l2.val
                l1= l1.next
                l2 = l2.next
                
                
            elif l1:
                if add:
                    val = l1.val+1
                else:
                    val = l1.val
                l1 = l1.next
            else:
                if add:
                    val = l2.val+1
                else:
                    val = l2.val
                l2 = l2.next
            
            if val>=10:
                curr.next = ListNode(val-10)
                add =True
            else:
                curr.next = ListNode(val)
                add = False
            curr = curr.next
            
        if add:
            curr.next = ListNode(1)
            
        return ans
                
        
                
                
                    
            
                
                
            
            
            
            
            