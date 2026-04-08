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
                wild = w[:j] + '*' + w[j + 1:]
                adjList[wild].append(w)
        
        q = deque([beginWord])
        seen = set([beginWord])

        while q:
            res += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return res
                
                for j in range(len(w)):
                    wild = w[:j] + '*' + w[j + 1:]

                    for child in adjList[wild]:
                        if child not in seen:
                            q.append(child)
                            seen.add(child)
        
        return 0
        