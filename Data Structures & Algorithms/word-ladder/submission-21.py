import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        adjList = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                wildcard = w[:i] + "*" + w[i + 1:]
                adjList[wildcard].append(w)
        
        q = deque()
        q.append(beginWord)
        seen = set()
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w== endWord:
                    return res
                if w in seen:
                    continue 
                seen.add(w)

                for i in range(len(w)):
                    wildcard = w[:i] + "*" + w[i + 1:]

                    for ch in adjList[wildcard]:
                        if ch not in seen:
                            q.append(ch)

        return 0
        
        