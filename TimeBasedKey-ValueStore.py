from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        self.time_timestamps = defaultdict(list)
        self.time_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_timestamps[key].append(timestamp)
        self.time_values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_timestamps:
            return ""
        left = 0
        right = len(self.time_timestamps[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.time_timestamps[key][mid] == timestamp:
                return self.time_values[key][mid]
            elif self.time_timestamps[key][mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if left == 0:
            return ""
        return self.time_values[key][left - 1]


timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
print(timeMap.get("alice", 1))
print(timeMap.get("alice", 2))
