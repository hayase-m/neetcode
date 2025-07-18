from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{str(len(s))}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find("#", i)
            parts_len = int(s[i:delimiter_pos])
            str_start = delimiter_pos + 1
            str_end = str_start + parts_len
            parts_str = s[str_start:str_end]
            result.append(parts_str)
            i += len(str(parts_len)) + 1 + len(parts_str)
        return result


strs = ["neet", "code", "love", "you"]
s = Solution().encode(strs)
print(s)
dc_strs = Solution().decode(s)
print(dc_strs)
