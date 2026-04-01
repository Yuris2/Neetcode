# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #Implement preorder traversal
        res = []
        def dfs(root):
            if not root:
                res.append('N')
                return None
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return root
        
        dfs(root)
        return "|".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stream = data.split('|')
        self.pre = 0

        def dfs():
            #If we hit a null node, return N
            #Don't forget to increment
            if stream[self.pre] == 'N':
                self.pre += 1
                return None
            
            #Create a node
            root = TreeNode(int(stream[self.pre]))
            #Increment to next node in preorder
            self.pre += 1
            #Attach left and right node (pre is incremented)
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()

            