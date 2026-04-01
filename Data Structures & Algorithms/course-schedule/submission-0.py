import collections

class Solution:
    def canFinish(self, numCourses: int, courses: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for c, p in courses:
            adj_list[c].append(p)
        
        #Constants 
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        #Marking courses as unvisisted
        states = [UNVISITED] * numCourses

        def dfs(node):
            currentState = states[node]

            if currentState == VISITED:
                return True
            if currentState == VISITING:
                return False
            
            #Mark node as a visiting
            states[node] = VISITING

            for n in adj_list[node]:
                if not dfs(n):
                    return False
            
            states[node] = VISITED
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        