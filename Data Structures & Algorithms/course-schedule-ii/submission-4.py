import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        res = []
        #course -> prer
        for course, pre in prerequisites:
            adjList[course].append(pre)
        
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
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
