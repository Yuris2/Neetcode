class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Return all unique combinations of candidates where chosen sum == target
        res = []
        stack = []

        candidates.sort()

        def back(i, total):
            if total == target:
                res.append(stack.copy())
                return 
            if i >= len(candidates):
                return
            
            stack.append(candidates[i])
            back(i + 1, total + candidates[i])
            stack.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1   
            back(i + 1, total)         
        
        back(0,0)
        return res
        