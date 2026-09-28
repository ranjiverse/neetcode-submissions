class TimeMap:

    def __init__(self):
        self.time_map = OrderedDict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))
  
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        all_values = self.time_map[key]
        l, r = 0, len(all_values) - 1
        res = ""
        while l <= r :
            mid = (l + r) // 2
            if all_values[mid][0] == timestamp :
                return all_values[mid][1]
            if all_values[mid][0] > timestamp :
                r = mid - 1
            else :
                res = all_values[mid][1]
                l = mid+1
        return res
    