# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque as queue
        
        
        
        
        if not root:
            return []
        
        q= queue()
        q.append([root])
        ans = [[root.val]]
        
        l = 1
        
        while q:
            
            x = q.popleft()
            res = []
            y = queue()
            l+=1
            
            for i in x:
                
                
                
                
                if l%2==0:
                    
                    if i.right:
                        y.appendleft(i.right)
                        res.append(i.right.val)
                        
                    if i.left:
                        y.appendleft(i.left)
                        res.append(i.left.val)
                        
                else:
                    if i.left:
                        y.appendleft(i.left)
                        res.append(i.left.val)
                        
                    if i.right:
                        y.appendleft(i.right)
                        res.append(i.right.val)
                        
            if res:
                        
                ans.append(res)
                q.append(y)
                
        return ans
            
            
            
            
        
        