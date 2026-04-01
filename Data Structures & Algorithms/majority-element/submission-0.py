class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = (len(nums) // 2) + 1
        majElt = None
        size_dict = {}

        for elt in nums:
            if elt in size_dict:
                size_dict[elt] += 1
            else:
                size_dict[elt] = 1
            if majElt is None or size_dict[elt] > size_dict[majElt]:
                majElt = elt
        
        return majElt