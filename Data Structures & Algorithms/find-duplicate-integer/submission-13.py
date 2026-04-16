class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #index -> index of next
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        find = 0
        while True:
            slow = nums[slow]
            find = nums[find]

            if slow == find:
                return find

        return