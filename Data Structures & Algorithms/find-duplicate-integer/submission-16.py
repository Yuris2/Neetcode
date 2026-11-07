class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #[Index] the value
        #[Value] the index pointed to
        # 0.   1.   2    3   4
        #[1,   2,   3,   2,  2]

        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2
        