class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R,C = len(board), len(board[0])
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        seen = set()
        res = set()

        def dfs(r,c,node,w):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 
            ch = board[r][c]
            if ch not in node.children or (r,c) in seen:
                return 
            
            node = node.children[ch]
            w += ch

            if node.endOfWord:
                res.add(w)

            seen.add((r,c))

            dfs(r+1,c,node, w) 
            dfs(r,c+1,node, w) 
            dfs(r-1,c,node, w) 
            dfs(r,c-1,node, w)

            seen.remove((r,c))
        
        for r in range(R):
            for c in range(C):
                dfs(r,c, root, "")
                
        return list(res)




        