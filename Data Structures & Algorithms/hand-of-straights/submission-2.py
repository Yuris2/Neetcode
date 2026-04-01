import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for n in sorted(hand):
            if count[n] != 0:
                for num in range(n, n + groupSize):
                    if count[num] <= 0:
                        return False
                    count[num] -= 1

        return True        