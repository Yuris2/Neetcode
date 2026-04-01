# create a set
# iterate through each element in the 'nums' array, adding each to the set
# through each iteration, check to see if the next element has already been added to the set
# once this happens, return True
# if not return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for n in nums:
            if n in unique:
                return True
            unique.add(n)
        return False


