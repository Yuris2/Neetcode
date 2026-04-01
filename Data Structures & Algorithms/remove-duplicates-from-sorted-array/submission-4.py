class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)

# convert array to set for unique values and have it sorted
# 
# take the values from the set and put it in an array