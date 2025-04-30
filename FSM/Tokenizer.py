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
            print(f"Erro encontrado na linha {line} coluna {e.column}")
            print(f"Expected: {e.expected}")
            print(" "*4, input_string.strip())
            print(" "*4, " "*(e.column - 2), "^")
