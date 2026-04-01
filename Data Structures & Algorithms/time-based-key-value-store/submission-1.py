class TimeMap:

    def __init__(self):
        #Key = Key
        #Value = [TimeStamp, Value]
        self.time = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time:
            self.time[key].append([timestamp, value])
        else:
            self.time[key] = [[timestamp, value]]
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.time:
            arr = self.time[key]
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m][0] > timestamp:
                    r = m - 1
                else:
                    res = arr[m][1]
                    l = m + 1
        
        return res

        
