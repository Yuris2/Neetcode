class Solution:
    def findOrder(self, numCourses: int, courses: List[List[int]]) -> List[int]:
        res = []
        adj_list = defaultdict(list)

        for c, prereq in courses:
            adj_list[c].append(prereq)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            currentState = states[node]
            if currentState == VISITED:
                return True
            if currentState == VISITING:
                return False
            
            states[node] = VISITING
            for connects in adj_list[node]:
                if not dfs(connects):
                    return False
            
            states[node] = VISITED
            res.append(node)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return res
        