class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()

        for n in nums:
            if n in dupe:
                return True
            else:
                dupe.add(n)
        
        return False
        