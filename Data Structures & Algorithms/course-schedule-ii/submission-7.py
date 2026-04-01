import collections

class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        #Key = course, Value = [pre reqs]
        adjList = defaultdict(list)
        res = []

        for c,p in prereq:
            adjList[c].append(p)
        
        NEW = 0
        VISITING = 1
        DONE = 2

        states = [NEW] * (numCourses)

        def dfs(course):
            state = states[course]
            if state == VISITING:
                return False
            elif state == DONE:
                return True
            
            states[course] = VISITING

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            states[course] = DONE
            res.append(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []

        return res
            
            
        