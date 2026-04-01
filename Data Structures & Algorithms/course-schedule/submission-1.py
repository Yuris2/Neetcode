import collections

class Solution:
    def canFinish(self, numCourses: int, courses: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for course, prereq in courses:
            adj_list[course].append(prereq)
        
        #Constants
        NEW = 0
        VISITING = 1
        VISITED = 2

        #initializing all the course to be new
        states = [NEW] * numCourses

        def dfs(node):
            currentState = states[node]
            #No outbound edges
            if currentState == VISITED:
                return True
            #Cycle detected
            if currentState == VISITING:
                return False
            
            states[node] = VISITING

            #check neighbors and their states
            for n in adj_list[node]:
                #If there is a cycle detected in the neighbors
                if not dfs(n):
                    return False
            #no outbound edges that contain cycles
            states[node] = VISITED
            return True
            

            
        
        #Iterating through nubmer of couses
        for course in range(numCourses):
            #If there was a problem with DFS aka a cycle
            if not dfs(course):
                return False
            
        return True
        
        