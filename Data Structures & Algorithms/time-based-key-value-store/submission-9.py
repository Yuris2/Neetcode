import collections
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.timeMap:
            return res
        
        data = self.timeMap[key]
        l, r = 0, len(data) - 1

        while l <= r:
            m = (l + r) // 2
            time, val = data[m]

            if time <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1
        
        return res
        
