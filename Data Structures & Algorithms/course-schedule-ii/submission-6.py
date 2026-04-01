import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        res = []

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        NEW = 0
        VISITING = 1
        DONE = 2

        state = [NEW] * numCourses

        def dfs(course):
            if state[course] == VISITING:
                return False
            elif state[course] == DONE:
                return True
            
            state[course] = VISITING

            #Check prereq
            for p in adjList[course]:
                if not dfs(p):
                    return False
            
            res.append(course)
            state[course] = DONE
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
        
        

        