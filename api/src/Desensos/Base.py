class DescensoRecursivoBase:
    def __init__(self, s: str):
        self.s = s
        self.i = 0
        self.n = len(s)
    
    def getToken(self) -> str:
        if self.i < self.n:
            token = self.s[self.i]
            self.i += 1
            return token
        else:
            return None



