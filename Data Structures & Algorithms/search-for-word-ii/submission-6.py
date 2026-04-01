class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R,C = len(board), len(board[0])
        seen = set()
        res = set()
        root = TrieNode()

        for w in words:
            root.addWord(w)

        def dfs(r,c,word,node):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            ch = board[r][c]
            if (r,c) in seen or ch not in node.children:
                return

            seen.add((r,c))
            node = node.children[ch]
            word += ch
            if node.endOfWord:
                res.add(word)
    
            dfs(r+1,c,word,node) 
            dfs(r,c+1,word,node) 
            dfs(r-1,c,word,node) 
            dfs(r,c-1,word,node)
            
            seen.remove((r,c))
            return res
        
        for r in range(R):
            for c in range(C):
                dfs(r,c,"", root)

        return list(res)

            
            

        