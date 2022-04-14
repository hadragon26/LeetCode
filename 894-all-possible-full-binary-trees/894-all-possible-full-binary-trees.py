# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        
        dic ={0:[] ,1:[TreeNode()]}
        
        
        
        def dfs(node):
            
            if node in dic:
                return dic[node]
            res = []
            for i in range(node):
                l = node-i-1 
                
                left ,right = dfs(l),dfs(i)
                
                for t1 in left:
                    for t2 in right:
                        res.append(TreeNode(0,t1,t2))
                        
            dic[node] = res
            return res
        
        
        return dfs(n)
            