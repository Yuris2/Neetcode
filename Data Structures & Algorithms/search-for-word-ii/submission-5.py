class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, w):
        curr = self
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        R,C = len(board), len(board[0])
        seen = set()
        res = set()

        for w in words:
            root.addWord(w)
        
        def dfs(r,c, node, word):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if (r,c) in seen or board[r][c] not in node.children:
                return 
            
            ch = board[r][c]
            seen.add((r,c))
            word += ch
            node = node.children[ch]

            if node.endOfWord:
                res.add(word)
            
            dfs(r+1,c,node, word)
            dfs(r-1,c,node, word)
            dfs(r,c+1,node, word)
            dfs(r,c-1,node, word)

            seen.remove((r,c))
            return
        
        for r in range(R):
            for c in range(C):
                dfs(r,c, root, "")
        
        return list(res)

            

            
        