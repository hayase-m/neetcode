from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        for key in sorted_keys:
            num_groups = count[key]
            if num_groups == 0:
                continue
            for i in range(key, key + groupSize):
                if count.get(i, 0) < num_groups:
                    return False
                count[i] -= num_groups
        return True


hand = [1, 2, 4, 2, 3, 5, 3, 4]
groupSize = 4
print(Solution().isNStraightHand(hand, groupSize))
