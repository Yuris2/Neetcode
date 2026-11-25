import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for n in sorted(hand):
            if count[n] == 0:
                continue
            
            for num in range(n, groupSize + n):
                if num not in count or count[num] == 0:
                    return False
                count[num] -=1
        
        return True
        