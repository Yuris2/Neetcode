import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        #Course -> Pre_req
        adjList = defaultdict(list)

        for c, p in prerequisites:
            adjList[c].append(p)
        
        NEW = 0
        VISITING = 1
        DONE = 2

        states = [NEW] * numCourses

        def dfs(course):
            if states[course] == DONE:
                return True
            elif states[course] == VISITING:
                return False
            
            states[course] = VISITING

            for c in adjList[course]:
                if not dfs(c):
                    return False
            
            states[course] = DONE
            res.append(course)
            return True
        
        for n in range(numCourses):
            #Detect cycle
            if not dfs(n):
                return []
        
        return res
        