import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adjList = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                wildcard = w[:i] + '*' + w[i + 1:]
                adjList[wildcard].append(w)
        
        res = 0
        seen = set([beginWord])

        q = deque([beginWord])
        
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    wildcard = word[:i] + '*' + word[i + 1:]

                    for w in adjList[wildcard]:
                        if w not in seen:
                            q.append(w)
                            seen.add(w)

        return 0

                
                    
        

        