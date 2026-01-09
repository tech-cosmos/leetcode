from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr=self.store[key]
        # l,r=0,len(arr)-1
        # current=""
        # while l<=r:
        #     mid=(l+r)//2
        #     times_mid, times_value=arr[mid]
        #     if timestamp<times_mid:
        #         r=mid-1
        #     else:
        #         print("Setting Current ",times_value)
        #         l=mid+1
        #         current=times_value
        i=bisect_right(arr,(timestamp,chr(255)))-1
        if i>=0:
            return arr[i][1]
        return ""




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)