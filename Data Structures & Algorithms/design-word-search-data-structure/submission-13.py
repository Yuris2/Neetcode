class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dp(j,node):
            curr = node

            for i in range(j,len(word)):
                ch = word[i]
                
                if ch == '.':
                    for child in curr.children.values():
                        if dp(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.endOfWord
            
        return dp(0,self.root)
        
