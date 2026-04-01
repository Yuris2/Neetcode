# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Preorder = [Root, (Left Subtree), (Right Subtree)]
        #Inorder = [(Left Subtree), Root, (Right Subtree)]
        inorderIndex = {}
        for i, elem in enumerate(inorder):
            inorderIndex[elem] = i
        
        self.preIndex = 0

        def dfs(l,r):
            #Base Case (Leaf Node)
            if l > r:
                return None
            
            #Get the value of the root
            rootVal = preorder[self.preIndex]
            #Get the midpoint
            mid = inorderIndex[rootVal]
            #Increment
            self.preIndex += 1
            #Construct the Tree
            root = TreeNode(rootVal)
            #Left of the inorder partition
            root.left = dfs(l, mid - 1)
            #Right of the inorder partition
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)

        