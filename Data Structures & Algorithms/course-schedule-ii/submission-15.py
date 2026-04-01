import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        #Course -> Pre
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visiting = set()
        done = set()


        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True
            
            visiting.add(course)

            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            done.add(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
        