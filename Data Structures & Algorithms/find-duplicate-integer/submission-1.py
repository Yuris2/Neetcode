class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's algorithm
        #Treat each index [i] as the value of a node a
        #Treat each value as the value that node points to
        #Fast and Slow Pointer Approach

        slow = fast = 0
        #index = node,val. 
        #val = node.next

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break
        
        #Since slow is already in a cycle, we just need to send another pointer into that cycle
        slow2 = 0
        while True:
           slow = nums[slow]
           slow2 = nums[slow2]

           if slow == slow2:
            return slow2

        