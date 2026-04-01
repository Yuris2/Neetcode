class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Fast and Slow Pointer algorithm to find the cycle
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        #send a pointer to slow
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        
        return 
        