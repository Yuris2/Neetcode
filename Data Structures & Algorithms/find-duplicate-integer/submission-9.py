class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Index of numss
        #Val = Index pointed to

        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break
        
        find = 0
        while True:
            slow = nums[slow]
            find = nums[find]

            if find == slow:
                return find

        return False       
        