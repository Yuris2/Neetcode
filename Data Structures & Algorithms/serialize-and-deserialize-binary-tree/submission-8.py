# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []

        def dfs(node):
            if not node:
                data.append('N')
                return
            
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "|".join(data)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stream = data.split('|')
        self.pre = 0

        def dfs():
            if stream[self.pre] == 'N':
                self.pre += 1
                return None
            
            root = TreeNode(int(stream[self.pre]))
            self.pre += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
