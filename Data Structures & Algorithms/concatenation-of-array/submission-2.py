class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for num in nums[:]:
            nums.append(num)
        return nums