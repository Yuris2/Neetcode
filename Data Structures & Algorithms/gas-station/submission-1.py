class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Verify that a solution exist
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0

        for i in range(len(gas)):
            #Get diff
            total += (gas[i] - cost[i])

            #If our total is neg, restart and try next station
            if total < 0:
                start = i + 1
                total = 0
        
        #Start will be left at the index that's total is pos from start to end
        return start

        