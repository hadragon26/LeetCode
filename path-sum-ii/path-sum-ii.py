# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        if not root:
            return None 
        
        ans = []
        
        
        
        def helper(root,target,res):
            
            
            if not root:
                return 
            
            if root:
                target-= root.val
            res.append(root.val)
            x = res.copy()
            
                
            if target==0 and root.right==root.left==None:
                ans.append(res)
                
            
            helper(root.left,target,res) 
            helper(root.right,target,x)
            
            
            
            
        helper(root,targetSum,[])
        
        return ans
        