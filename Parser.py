from Gramatics import Gramatics
from Table import Table
from FSM.Token import Token

class ParsingError(Exception):
    def __init__(self, message, expected=None):
        super().__init__(message)
        self.expected = expected
        
    def __str__(self):
        base = super().__str__()
        return f"{base} (Expected: {self.expected})"

class Parser:
    def __init__(self, gramatic: Gramatics):
        self.gramatic = gramatic
        self.table = Table(gramatic)

    def parse(self, input: list[Token]):

        stack = [self.gramatic.initial, "$"]

        # Filtra os tokens que não são quebras de linha e espaços vazios
        input = [x for x in input if x.type != 'LINEBREAK']
        
        while stack[0] != "$" and len(input) > 0:
            stackVal = stack.pop(0)
            inputType = input[0].type
            inputChar = input[0].value
            
            #Encontrou o simbolo terminal na árvore
            if stackVal == inputChar or (inputType == 'PROPOSITION' and stackVal == 'PROP_SYMBOL'):
                input.pop(0)
                continue

            if inputType == 'PROPOSITION':
                rule = self.table.getRule(stackVal, 'PROP_SYMBOL')
            else:
                rule = self.table.getRule(stackVal, inputChar)

            if rule == None:
                raise ParsingError('Erro semântico', expected=stackVal)

            for x in reversed(rule):
                stack.insert(0, x)

        if len(stack) > 1 or len(input) > 0:
            raise ParsingError('Erro semântico', expected=stackVal)

