class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        l = 0
        res = 0

        for r in range(len(fruits)):
            baskets[fruits[r]] = 1 + baskets.get(fruits[r], 0)

            while len(baskets) > 2:
                baskets[fruits[l]] -= 1

                if baskets[fruits[l]] <= 0:
                    del baskets[fruits[l]]
                
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
        