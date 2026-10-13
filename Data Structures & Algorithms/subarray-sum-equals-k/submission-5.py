class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = {0 : 1} # prefix sum : count
        prefix = 0

        for n in nums:
            prefix += n
            needed = prefix - k
            if needed in count:
                res += count[needed]
            count[prefix] = 1 + count.get(prefix, 0)

        return res


