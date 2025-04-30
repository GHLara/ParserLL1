class Token:
    def __init__(self, value, position, line, type):
        self.value = value
        self.type = type
        self.position = position
        self.line = line
