class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(candidates):
                return
            
            stack.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            stack.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)
        
        backtrack(0,0)
        return res
        