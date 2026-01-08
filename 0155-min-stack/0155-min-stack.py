import math
class MinStack:

    def __init__(self):
        self.a=[]
        self.small=[]

    def push(self, val: int) -> None:
        self.a.append(val)
        if len(self.small)==0:
            self.small.append(val)
        else:
            self.small.append(min(val,self.small[-1]))

    def pop(self) -> None:
        self.a.pop()
        self.small.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.small[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()