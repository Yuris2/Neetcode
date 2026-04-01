import collections

class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for course, pre in prereq:
            adjList[course].append(pre)
        
        NEW = 0
        VISITING = 1
        DONE = 2

        states = [NEW] * numCourses
        res = []

        def dfs(course):
            state = states[course]
            if state == VISITING:
                return False
            if state == DONE:
                return True
            
            states[course] = VISITING
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            states[course] = DONE
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
            
        