import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for card in sorted(hand):
            if count[card] != 0:
                for c in range(card, card + groupSize):
                    if count[c] == 0:
                        return False
                    count[c] -= 1
        
        return True



        