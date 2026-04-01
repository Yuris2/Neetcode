import collections

class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        res = []

        #Populating adjList
        for c, p in pre:
            adjList[c].append(p)
        
        NEW = 0
        PROCESS = 1
        DONE = 2

        states = [0] * numCourses

        def dfs(course):
            current = states[course]
            if current == PROCESS:
                return False
            if current == DONE:
                return True
            
            states[course] = PROCESS

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

