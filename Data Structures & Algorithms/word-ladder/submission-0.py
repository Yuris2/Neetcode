import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        #Check if endWord is not even in the wordList
        if endWord not in wordList:
            return res
        #Add the word to the wordList
        wordList.append(beginWord)

        adjList = defaultdict(list)   
        #Construct adjacency list 
        #{wildcard:list of words}
        for word in wordList:
            for j in range(len(word)):
                wildcard = word[:j] + "*" + word[j+1:]
                adjList[wildcard].append(word)
        
        q = deque([beginWord])
        seen = set([beginWord])

        while q:
            #Increase path by one
            res += 1
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                #See all possible wildcards
                for j in range(len(word)):
                    wildcard = word[:j] + "*" + word[j+1:]
                    
                    for child in adjList[wildcard]:
                        if child not in seen:
                            q.append(child)
                            seen.add(child)
    
        #Did not find a result
        return 0



        