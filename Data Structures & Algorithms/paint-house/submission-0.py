class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #[0] = Red
        #[1] = Blue
        #[2] = Green
        cache = {}

        def dfs(house, color):
            if house >= len(costs):
                return 0
            if (house,color) in cache:
                return cache[(house, color)]
            
            res = 2e9 

            for i, cost in enumerate(costs[house]):
                if i != color:
                    res = min(res, cost + dfs(house + 1, i))
                    cache[(house, color)] = res
            
            return res
        
        return dfs(0, -1)
            

            

        