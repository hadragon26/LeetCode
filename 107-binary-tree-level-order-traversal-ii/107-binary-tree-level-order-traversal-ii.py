# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque as queue
        
        
        if not root:
            return []
        
        
        
        q = queue()
        q.append([root])
        
        ans = queue([[root.val]])
        while q:
            
            y = []
            z = []
            x = q.popleft()
            
            for i in x:
                
                if i.left:
                    y.append(i.left)
                    z.append(i.left.val)
                    
                    
                    
                if i.right:
                    y.append(i.right)
                    z.append(i.right.val)
                    
                    
            if y:
                ans.append(z)
                q.append(y)
        ans.reverse()
        return ans
            
        