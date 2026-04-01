# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, node: Optional[TreeNode]) -> str:
        res = []
        #Pre order traversal
        def dfs(root):
            if not root:
                res.append('N')
                return None
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return root
        
        dfs(node)
        return "|".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stream = data.split('|')
        #Track index of preorder traversal
        self.pre = 0

        def dfs():
            if stream[self.pre] == 'N':
                self.pre += 1
                return None
            
            #Create a node
            root = TreeNode(int(stream[self.pre]))
            self.pre += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
