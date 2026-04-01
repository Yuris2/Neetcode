import collections

class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #Timestamp in increasing order
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #Most recent time stamp <= timestmap
        res = ""
        if key in self.timemap:
            data = self.timemap[key]

            l,r = 0, len(data) - 1

            while l <= r:
                m = (l + r) // 2

                if data[m][0] == timestamp:
                    res = data[m][1]
                    break
                elif data[m][0] < timestamp:
                    res = data[m][1]
                    l = m + 1
                else:
                    r = m - 1
            
        return res
        
