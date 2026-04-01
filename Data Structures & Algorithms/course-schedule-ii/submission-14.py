import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        #Course -> Pre
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        NEW, PROCESSING, DONE = 0,1,2

        states = [NEW] * numCourses

        def dfs(course):
            state = states[course]

            if state == PROCESSING:
                return False
            if state == DONE:
                return True
            
            states[course] = PROCESSING

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
        