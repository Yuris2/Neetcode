class TrieNode:
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
        root = TrieNode()

        for w in words:
            root.addWord(w)

        res = set()
        seen = set()
        def backtrack(r,c,word,node):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 
            if (r,c) in seen or board[r][c] not in node.children:
                return
            
            seen.add((r,c))
            ch = board[r][c]
            word += ch
            node = node.children[ch]

            if node.endOfWord:
                res.add(word)

            backtrack(r+1,c,word,node)
            backtrack(r,c+1,word,node)
            backtrack(r-1,c,word,node)
            backtrack(r,c-1,word,node)

            seen.remove((r,c))

        for r in range(R):
            for c in range(C):
                backtrack(r,c,"",root)
        
        return list(res)
        