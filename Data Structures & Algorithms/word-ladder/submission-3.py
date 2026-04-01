import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        if endWord not in wordList:
            return res
        
        adjList = defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for j in range(len(w)):
                wildcard = w[:j] + '*' + w[j + 1:]
                adjList[wildcard].append(w)
        
        q = deque([beginWord])
        seen = set([beginWord])

        while q:
            res += 1

            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return res
                
                for j in range(len(w)):
                    wildcard = w[:j] + '*' + w[j + 1:]

                    for word in adjList[wildcard]:
                        if word not in seen:
                            q.append(word)
                            seen.add(word)
        
        return 0

        