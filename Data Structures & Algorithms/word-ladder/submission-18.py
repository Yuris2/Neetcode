import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        if endWord not in wordList:
            return res
        #You can transform any word to another word given they only differ by one char
        #Return number of transformations

        #Adjlist of wildcard to words
        adjList = defaultdict(list)

        #Create wildcard
        for w in wordList:
            for i in range(len(w)):
                wC = w[:i] + "*" + w[i+1:]
                adjList[wC].append(w)

        seen = set({beginWord})
        q = deque()
        q.append(beginWord)

        while q:
            res += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return res
                
                for i in range(len(w)):
                    wC = w[:i] + "*" + w[i+1:]
                    
                    for ch in adjList[wC]:
                        if ch not in seen:
                            q.append(ch)
                            seen.add(ch)
        
        return 0


    

        