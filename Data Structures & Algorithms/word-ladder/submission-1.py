import collections
class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        res = 0
        if end not in wordList:
            return res
        #Add start to word list
        wordList.append(start)
        adjList = defaultdict(list)

        #Construct adjacency list
        for word in wordList:
            for j in range(len(word)):
                wildcard = word[:j] + '*' + word[j + 1:]
                adjList[wildcard].append(word)
        
        #Shortest path is BFS
        q = deque([start])
        seen = set([start])

        while q:
            res += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w == end:
                    return res
                
                for j in range(len(w)):
                    wildcard = w[:j] + '*' + w[j + 1:]

                    for adj in adjList[wildcard]:
                        if adj not in seen:
                            q.append(adj)
                            seen.add(adj)
        
        return 0

        