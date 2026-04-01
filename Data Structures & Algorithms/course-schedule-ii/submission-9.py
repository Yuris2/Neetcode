import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        states = [0] * numCourses
        res = []

        def dfs(node):
            if states[node] == 2:
                return True
            if states[node] == 1:
                return False
            
            states[node] = 1

            for pre in adjList[node]:
                if not dfs(pre):
                    return False
            
            res.append(node)
            states[node] = 2

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
        