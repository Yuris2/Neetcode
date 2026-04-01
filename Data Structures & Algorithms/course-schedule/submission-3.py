import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        #Course points to the pre req needed to take it
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        #never visited
        NEW = 0
        #not done visitng all edges
        VISITING = 1
        #All edges visited
        DONE = 2
        
        states = [NEW] * numCourses

        def dfs(course):
            if states[course] == VISITING:
                return False
            if states[course] == DONE:
                return True
            
            states[course] = VISITING

            for c in adjList[course]:
                #if cycle is detected
                if not dfs(c):
                    return False
            
            states[course] = DONE
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        

        