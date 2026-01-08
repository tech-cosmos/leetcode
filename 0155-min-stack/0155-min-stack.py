import math
class MinStack:

    def __init__(self):
        self.a=[]
        self.small=math.inf

    def push(self, val: int) -> None:
        self.a.append(val)
        self.small=min(val,self.small)

    def pop(self) -> None:
        self.a.pop()
        if len(self.a)>0:
            self.small=min(self.a)
        else:
            self.small=math.inf

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.small


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()