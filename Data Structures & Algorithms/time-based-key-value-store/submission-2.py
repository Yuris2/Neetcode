class TimeMap:

    def __init__(self):
        #Key = key, value = [(timestamp, value)]
        self.timeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp,value))
    
    def get(self, key: str, timestamp: int) -> str:
        prev_timestamp = ""
        if key in self.timeMap:
            occ = self.timeMap[key]

            l, r = 0, len(occ) - 1

            while l <= r:
                m = (l + r) // 2

                curr = occ[m][0]

                if curr == timestamp:
                    #Return key associated with timestamp
                    return occ[m][1]
                elif curr > timestamp:
                    r = m - 1
                else:
                    prev_timestamp = occ[m][1]
                    l = m + 1
        
        return prev_timestamp

                
