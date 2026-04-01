import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        adjList = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                wildcard = word[:j] + '*' + word[j + 1:]
                adjList[wildcard].append(word)
        
        q = deque([beginWord])
        seen = set([beginWord])
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    wildcard = word[:j] + '*' + word[j + 1:]

                    for w in adjList[wildcard]:
                        if w not in seen:
                            q.append(w)
                            seen.add(w)

        
        return 0
        
        