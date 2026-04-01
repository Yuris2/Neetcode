import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        res = []

        for course, pre in prerequisites:
            adjList[course].append(pre)
        
        NEW = 0
        VISITING = 1
        DONE = 2

        states = [NEW] * numCourses

        def dfs(course):
            state = states[course]

            if state == DONE:
                return True
            elif state == VISITING:
                return False
            
            states[course] = VISITING

            for neighbor in adjList[course]:
                if not dfs(neighbor):
                    return False
            
            states[course] = DONE
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
        