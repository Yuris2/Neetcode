'''
    #If sum of path is == target, add path to the res and return
    #One decision would be do we include this number
        #We want to stay at the current index
    #Other do we want to check the other numbers
        #Move forward in the index
    
    #We have to check forward in the nums array
    #[2,2,5]
    #[5,2,2]
    [2,5,6,9]               []


                2       5       6       []
            
        [2,2]       [2]
    
    [2,2,2]     [2,5]   [2]
'''




class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Backtracking
        res = []
        path = []

        def back(i, total):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(nums) or total > target:
                return

            path.append(nums[i])
            back(i, total + nums[i])
            path.pop()
            back(i + 1, total)
        
        back(0, 0)
        return res

        

            


        

        