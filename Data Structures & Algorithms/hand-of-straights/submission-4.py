import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for c in sorted(hand):
            if count[c] != 0:
                for card in range(c, c + groupSize):
                    if count[card] <= 0:
                        return False
                    count[card] -= 1
        
        return True

