import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        #Pattern
            #BFS on the transformations of characters within a word
        
        #General Idea
            #Create an adjList of wildcard to word 
            #Wildcard represents the transformations you can take from a certain word
            #Run BFS from start to endWord returning number of layers
        
        adjList = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                wild = w[:i] + "*" + w[i + 1:]
                adjList[wild].append(w)
        
        queue = deque([beginWord])
        seen = set([beginWord])
        res = 0

        while queue:
            res += 1
            for _ in range(len(queue)):
                w = queue.popleft()

                if w == endWord:
                    return res
                

                for i in range(len(w)):
                     wild = w[:i] + "*" + w[i + 1:]

                     for word in adjList[wild]:
                        if word not in seen:
                            seen.add(word)
                            queue.append(word)
        
        return 0




        