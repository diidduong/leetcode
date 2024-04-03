from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map[key]:
            return ''

        arr = self.hash_map[key]
        res = ''
        start = 0
        end = len(arr) - 1
        mid = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
