class DescensoRecursivoBase:
    def __init__(self, s: str, i: int = 0):
        self.s = s
        self.i = i
        self.n = len(s)
    
    def getToken(self) -> str:
        if self.i < self.n:
            token = self.s[self.i]
            self.i += 1
            return token
        else:
            return None
    
    def copy(self):
        return DescensoRecursivoBase(self.s, self.i)



