import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()

        for card in hand:
            if count[card] != 0:
                for c in range(card, card + groupSize):
                    if count[c] != 0:
                        count[c] -= 1
                    else:
                        return False
        
        return True
        