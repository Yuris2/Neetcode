import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        if endWord not in wordList:
            return res 

        wordList.append(beginWord)
        adjList = defaultdict(list)

        for w in wordList:
            for j in range(len(w)):
                wild = w[:j] + '*' + w[j + 1:]
                adjList[wild].append(w)
        
        seen = set([beginWord])
        q = deque([beginWord])

        while q:
            res += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return res
                
                for j in range(len(w)):
                    wild = w[:j] + '*' + w[j + 1:]
                
                    for word in adjList[wild]:
                        if word not in seen:
                            q.append(word)
                            seen.add(word)
        
        return 0



        

        