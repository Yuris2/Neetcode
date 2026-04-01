class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = set()
        end = len(nums)
        i = 0
        while i < end:
            if nums[i] in found:
                nums.pop(i)
                end -= 1
            else:
                found.add(nums[i])
                i += 1
        return len(nums)

        