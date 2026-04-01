import collections

class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        res = []

        for c, p in prereq:
            adjList[c].append(p)
        
        NEW, VISITING, DONE = 0, 1, 2
        states = [NEW] * numCourses

        def dfs(course):
            state = states[course]
            if state == VISITING:
                return False
            if state == DONE:
                return True
            
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
        