import sys
from FSM.FiniteStateMachine import FiniteStateMachine
from FSM.FiniteStateMachine import TokenizationError
from FSM.Token import Token


class Tokenizer:
    def __init__(self):
        self.tokens: list[Token] = []

    def tokenize(self, input_string, line):
        fsm = FiniteStateMachine()
        try:
            tokens = fsm.startMachine(input_string)
            for token in tokens:
                tokenObj = Token(
                    value=token.get("value"),
                    type=token.get("type"),
                    position=token.get("position"),
                    line=line
                )
                self.tokens.append(tokenObj)

        except TokenizationError as e:
            print(f'Erro sintático: linha {line} coluna {e.column}')
            print(f"Token não identificado: '{input_string.strip()}'",)
            sys.exit(1)

    def readFile(self, path):
        with open(path, 'r') as file:
            for line_index, line in enumerate(file):
                self.tokenize(line, line_index)
