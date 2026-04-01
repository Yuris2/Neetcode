#[1,2,3,2]

'''
#Index      #Number
0               1           2           
1               2           
2               3           s,f
3               2


slow
fast
'''
#slow
#fast


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Index -> index
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

            if slow2 == slow:
                return slow
        