import collections

class TimeMap:

    def __init__(self):
        #Multiple Values for the Same key at given Timestamp
        self.time = defaultdict(list)
        #Retrieving key's values at timestamp
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        metadata = self.time[key]

        l,r = 0, len(metadata) - 1

        while l <= r:
            m = (l + r) // 2

            if metadata[m][0] > timestamp:
                r = m - 1
            else:
                res = metadata[m][1]
                l = m + 1
        
        return res
        
