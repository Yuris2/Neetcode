import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        res = []

        NONE = 0
        PENDING = 1
        DONE = 2

        states = [NONE] * numCourses

        def dfs(node):
            currentState = states[node]
            if currentState == DONE:
                return True
            
            if currentState == PENDING:
                return False
            
            states[node] = PENDING

            for children in adj_list[node]:
                if not dfs(children):
                    return False
            
            states[node] = DONE
            res.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
        