import collections
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.store:
            metadata = self.store[key]
            l,r = 0, len(metadata) - 1

            while l <= r:
                m = (l + r) // 2

                if metadata[m][0] == timestamp:
                    res = metadata[m][1]
                    return res
                elif metadata[m][0] < timestamp:
                    res = metadata[m][1]
                    l = m + 1
                else:
                    r = m - 1
        
        return res
                
        
