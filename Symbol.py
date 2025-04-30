class Symbol:
    def __init__(self, name, isTerminal, isInitial=False):
        self.name = name
        self.isTerminal = isTerminal
        self.isInitial = isInitial
