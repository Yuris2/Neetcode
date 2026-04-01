class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Treat the array as a linked list
        #[0,1,2,3,4]
        #[1,3,4,2,2]

        '''
        0 -> 1 -> 3 -> 2 -> 4 
                         <-
                    s               f
        2 -> 4
        '''
        #The duplicate number is the one that is the start/entrance of a cycle
        #Use slow and fast pointer
        slow = fast = 0
        #Pointers will overlap at start of cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        #Floyd's Algo only guarantees existence of cycle not the entrance
        find = 0
        while True:
            slow = nums[slow]
            find = nums[find]

            if find == slow:
                return find
            
        return None
        