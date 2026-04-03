import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Rearrange the cards into groups
        #Groups have to be the size of groupSize
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for card in sorted(hand):
            #If we can still use a card
            if count[card] != 0:
                for c in range(card, card + groupSize):
                    if count[c] <= 0:
                        return False
                    count[c] -= 1
        
        return True
        #Card Values are Consecutive Increasing by 1
        #Keep Track of how many cards we have
        