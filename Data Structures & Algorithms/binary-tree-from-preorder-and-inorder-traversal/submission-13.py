# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#[root, left s.t, right s.t]
#[left s.t, root, right s.t] (inorder)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderVal = {}

        for i, v in enumerate(inorder):
            inorderVal[v] = i
        
        self.pre = 0

        def dfs(l,r):
            if l > r:
                return None
            
            rootVal = preorder[self.pre]
            node = TreeNode(rootVal)
            self.pre += 1

            m = inorderVal[rootVal]
            node.left = dfs(l, m - 1)
            node.right = dfs(m + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)


        