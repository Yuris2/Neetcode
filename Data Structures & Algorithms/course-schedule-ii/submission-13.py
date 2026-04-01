import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for c, p in prerequisites:
            adjList[c].append(p)
        
        NEW, VISITING, DONE = 1,2,3
        states = [NEW] * numCourses

        res = []

        def dfs(course):
            state = states[course]
            if state == DONE:
                return True
            if state == VISITING:
                return False
            
            states[course] = VISITING

            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            
            states[course] = DONE
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
            

        