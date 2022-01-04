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
        if not root:
            return None
        q = []
        
        q.append(root)
        tail = root
            
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if tail == node:
                node.next = None
                if len(q) > 0:
                    tail = q[-1]
            else:
                node.next = q[0]
        return root
        
        