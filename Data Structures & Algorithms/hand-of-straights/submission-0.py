import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Check if we can even form valid groups
        if len(hand) % groupSize != 0:
            return False
        
        #Count num: freq
        count = Counter(hand)

        hand.sort()
        #We are going to check if we have an available card (count > 0)
        #Force form a group (num to num + groupSize - 1)
            #IF count of any of the num in the group < 0: can't form group

        for n in hand:
            #Form a new group, if count == 0, already in a group
            if count[n] != 0:
                #Loop enforces consecutive
                for num in range(n, n + groupSize):
                    #Can't form a group
                    if count[num] <= 0:
                        return False
                    #Decrement
                    count[num] -= 1
        
        return True



        