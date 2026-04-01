class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElt, freq = 0, 0
        for elt in nums:
            if freq == 0:
                majElt = elt
                freq += 1
            elif majElt == elt:
                freq += 1
            elif majElt != elt:
                freq -= 1
        return majElt
