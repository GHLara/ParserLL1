from Gramatics import Gramatics
from Table import Table
from FSM.Token import Token


class Parser:
    def __init__(self, gramatic: Gramatics, tokens: list[Token]):

        self.gramatic = gramatic
        self.table = Table(gramatic)

        self.stack = [self.gramatic.initial, "$"]
        self.input = tokens

    def view(self):
        # Filtra os tokens que não são quebras de linha e espaços vazios
        self.input = [x for x in self.input if x.type != 'LINEBREAK']

        while self.stack[0] != "$" and len(self.input) > 0:
            print('Input =>', [token.value for token in self.input])
            print('Stack =>', self.stack)
            print(' ')
            stackVal = self.stack.pop(0)
            inputType = self.input[0].type
            inputChar = self.input[0].value


            if stackVal == inputChar:
                self.input.pop(0)
                continue

            if inputType == 'PROPOSITION' and stackVal == 'PROP_SYMBOL':
                self.input.pop(0)
                continue

            if inputType == 'PROPOSITION':
                rule = self.table.getRule(stackVal, 'PROP_SYMBOL')
            else:
                rule = self.table.getRule(stackVal, inputChar)

            if rule == None:
                break

            for x in reversed(rule):
                self.stack.insert(0, x)

        print("Stack final =>", self.stack)
        print("Input final =>", self.input)

        if len(self.stack) > 1:
            invalid = self.stack.pop(0)
            print(f"Missing: {self.table.getFirst(invalid)}")

        if len(self.input) > 0:
            invalid = self.input.pop(0)
            print(f"Invalid: ", invalid.value)
            print(f"At Line: ", invalid.line)
            print(f"Column: ", invalid.position)
