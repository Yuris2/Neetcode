# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Preorder does not tell you where the left subtree ends and the right begin
        inIndex = {}

        for i, elem in enumerate(inorder):
            inIndex[elem] = i
        
        self.pre = 0

        def dfs(l,r):
            if l > r:
                return None
            
            node = TreeNode(preorder[self.pre])
            idx = inIndex[preorder[self.pre]]
            self.pre += 1

            node.left = dfs(l, idx - 1)
            node.right = dfs(idx + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)



        
               
            

        

        