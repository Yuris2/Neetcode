'''
[[17,2,17],[16,16,5],[14,3,19]]
                            .


                17          2           17

            16      5     16    5    16     16

        14    19  14  3  3  19. 14 3 3 19.  14    19


'''




class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cache = {}
        #index = house#,        #color = previous color chosen        
        def back(index, prevColor):
            if index >= len(costs):
                return 0
            if (index, prevColor) in cache:
                return cache[(index, prevColor)]
            
            res = 2e9
            for color, cost in enumerate(costs[index]):
                #Ensure we don't paint adjacent houses
                if color != prevColor:
                    res = min(res, cost + back(index + 1, color))
                    cache[(index, prevColor)] = res
            
            return res
        
        return back(0, -1)