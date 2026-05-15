class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True
    
    def search(self, word):
        def dfs(root, i):
            curr = root

            for j in range(i,len(word)):
                c = word[j]

                if c == '.':
                    for child in curr.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.endOfWord
        
        return dfs(self.root, 0)
        
