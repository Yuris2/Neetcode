class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set()
        for num in nums:
            allNums.add(num)
        res = 0
        for num in nums:
            if num not in allNums:
                continue
            cur = 1
            l, r = num - 1, num + 1
            while l in allNums:
                allNums.remove(l)
                cur += 1
                l -= 1
            while r in allNums:
                allNums.remove(r)
                cur += 1
                r += 1
            res = max(res, cur)
        return res