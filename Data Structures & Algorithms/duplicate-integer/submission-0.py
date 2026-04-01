class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for n in nums:
            dic[n] = 1 + dic.get(n,0)
            
        for k, v in dic.items():
            if v > 1:
                return True
        
        return False
        
         