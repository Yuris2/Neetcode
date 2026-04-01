class TimeMap:

    def __init__(self):
        self.time = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time:
            self.time[key].append([value, timestamp])
        else:
            self.time[key] = [[value,timestamp]]
        
    def get(self, key: str, timestamp: int) -> str:
        val = ""

        if key in self.time:
            arr = self.time[key]
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m][1] <= timestamp:
                    val = arr[m][0]
                    l = m + 1
                else:
                    r = m - 1
        
        return val



        
