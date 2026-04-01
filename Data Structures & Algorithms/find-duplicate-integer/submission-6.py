class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Find where the cycle starts and if there is a cycle
            #Fast and slow might
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow2
        
        return None

        