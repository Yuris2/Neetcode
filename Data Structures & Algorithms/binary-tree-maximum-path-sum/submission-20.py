# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #At each point, we have some decisions to make
        #The max path sum can be the following:
            #The current root sum + the right max + left max
            #The current sum += max(left, or right node)
        

        self.res = -2e9

        def dfs(node):
            if not node:
                return 0
            
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))

            self.res = max(self.res, left + right + node.val)

            return node.val + max(left,right)
        
        dfs(root)
        return self.res
        #Use DFS
            #Base Case:
                #if not root:
                    #Return 
            #check case 1. and update res if we found a new max
            #return the maximum between the left and right node up to previous node
            
        