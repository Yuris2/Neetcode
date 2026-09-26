import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        if endWord not in wordList:
            return res

        wordList.append(beginWord)
        #Wilcard to word
        adjList = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                wild = w[:i] + "*" + w[i + 1:]
                adjList[wild].append(w)
        
        q = deque()
        q.append(beginWord)
        seen = set()

        while q:
            res += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return res
                if w in seen:
                    continue
                
                seen.add(w)

                for i in range(len(w)):
                    wild = w[:i] + "*" + w[i + 1:]
                    
                    for word in adjList[wild]:
                        if word not in seen:
                            q.append(word)

        return 0


        







            

        