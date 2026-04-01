import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        NEW = 0
        VISITING = 1
        VISITED = 2

        states = [NEW] * numCourses

        def dfs(course):
            #Cycle detected
            if states[course] == VISITING:
                return False
            #no more edges leaving
            elif states[course] == VISITED:
                return True
            
            states[course] = VISITING

            for c in adjList[course]:
                if not dfs(c):
                    return False
            
            order.append(course)
            states[course] = VISITED
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return order


        