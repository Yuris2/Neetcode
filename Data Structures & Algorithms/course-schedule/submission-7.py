class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map course -> list of pre reqs
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visit set along the curr DFS path
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            # pre req list empty -> able to complete
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            # explore pre reqs
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            # mark as searched and completable
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



        
            



            

        


        


