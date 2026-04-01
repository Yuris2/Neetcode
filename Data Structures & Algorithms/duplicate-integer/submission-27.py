# create a set
# iterate through each element in the 'nums' array, adding each to the set
# through each iteration, check to see if the next element has already been added to the set
# once this happens, return True
# if not return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False

