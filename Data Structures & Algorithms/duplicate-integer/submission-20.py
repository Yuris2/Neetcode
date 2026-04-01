class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()

        for n in nums:
            if n in hset:
                return True

            hset.add(n) 

        return False