import collections
class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for c, p in prereq:
            adjList[c].append(p)
        
        NEW, VISITING, DONE = 0,1,2
        states = [NEW] * numCourses
        
        def dfs(course):
            if states[course] == DONE:
                return True
            if states[course] == VISITING:
                return False
            
            states[course] = VISITING

            for child in adjList[course]:
                if not dfs(child):
                    return False
            
            states[course] = DONE

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        
        