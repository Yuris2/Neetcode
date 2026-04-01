import collections

class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.time:
            data = self.time[key]

            l = 0
            r = len(data) - 1

            while l <= r:
                m = (l + r) // 2
                if data[m][0] == timestamp:
                    res = data[m][1]
                    break
                if data[m][0] < timestamp:
                    res = data[m][1]
                    l = m + 1
                else:
                    r = m - 1
        return res
            

        
