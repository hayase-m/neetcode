from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sortedでnlogn、forでmなのでO(m*nlogn)
        # result = defaultdict(list)
        # for str in strs:
        #     key = "".join(sorted(str))
        #     result[key].append(str)
        # return list(result.values())
        groups = defaultdict(list)
        for str in strs:
            count_char = [0] * 26
            for c in str:
                count_char[ord(c) - ord('a')] += 1
            groups[tuple(count_char)].append(str)
        return list(groups.values())


strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(Solution().groupAnagrams(strs))
