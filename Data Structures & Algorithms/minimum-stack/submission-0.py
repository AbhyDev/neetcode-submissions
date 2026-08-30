class MinStack:

    def __init__(self):
        self.ls=[]

    def push(self, val: int) -> None:
        if len(self.ls)==0:
            self.ls.append([val,val])
        else:
            mini=min(self.ls[-1][1],val)
            self.ls.append([val,mini])

    def pop(self) -> None:
        self.ls.pop()

    def top(self) -> int:
        return self.ls[-1][0]

    def getMin(self) -> int:
        return self.ls[-1][1]
