class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cache = {}
        def backtrack(house, color):
            if house == len(costs):
                return 0
            if (house, color) in cache:
                return cache[(house,color)]
            
            res = 2e9
            for i, cost in enumerate(costs[house]):
                if i != color:
                    #Take the minimum sum from this point
                    res = min(res, cost + backtrack(house + 1, i))
                    cache[(house,color)] = res
                    #Go down the path
                    #Undo decision
            
            return res
        
        return backtrack(0, -1)
        



        