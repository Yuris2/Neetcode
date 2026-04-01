# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Preorder = [Root, (Left Subtree), (Right Subtree)]
#Inorder =  [(Left Subtree), Root, (Right Subtree)]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderToIndex = {}
        self.pre = 0

        for i, elem in enumerate(inorder):
            inorderToIndex[elem] = i
        
        def dfs(l,r):
            if l > r:
                return None
            
            rootVal = preorder[self.pre]
            root = TreeNode(rootVal)
            self.pre += 1

            mid = inorderToIndex[rootVal]

            #The left subtree is to the left of inorder
            root.left = dfs(l, mid - 1)
            #The right subtree is to the right of inorder
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)
        