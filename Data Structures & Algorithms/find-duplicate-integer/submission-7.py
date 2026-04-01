class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        search = 0

        while True:
            slow = nums[slow]
            search = nums[search]

            if slow == search:
                return search
        