import collections

class TimeMap:

    def __init__(self):
        #multiple values with same key at time
        #Retrieve value at timestamp
        #Guaranteed timestamps are in increasing order in set

        #Key = key, Value = [timestamp, value]
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.timeMap:
            metadata = self.timeMap[key]
            #Initialize BS
            l,r = 0, len(metadata) - 1

            while l <= r:
                m = (l + r) // 2

                if metadata[m][0] == timestamp:
                    res = metadata[m][1]
                    break
                elif metadata[m][0] < timestamp:
                    res = metadata[m][1]
                    l = m + 1
                else:
                    r = m - 1
        
        return res
        
