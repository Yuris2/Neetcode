import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #If it is not even divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for n in sorted(hand):
            #We haven't used up all of this card
            if count[n] != 0:
                #Use up every card in the group
                for num in range(n, n + groupSize):
                    #If we don't have that card
                    if count[num] <= 0:
                        return False
                    #Decrement
                    count[num] -= 1
        
        return True
        


        