class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Treat as a linked list

        #Node
            #.val = index
            #.next = index
        
        #Slow/Pointer to detect Cycle
        #Send second pointer for cycle

        slow = fast = nums[0]

        # Find intersection inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find entrance to cycle = duplicate
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

        