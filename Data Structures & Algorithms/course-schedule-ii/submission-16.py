import collections
class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for c, p in prereq:
            adjList[c].append(p)
        
        NEW, VISITING, DONE = 0,1,2
        states = [NEW] * numCourses
        res = []
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
            res.append(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
        
        