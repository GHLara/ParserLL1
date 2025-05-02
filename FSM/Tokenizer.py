from FSM.FiniteStateMachine import FiniteStateMachine
from FSM.FiniteStateMachine import TokenizationError
from FSM.Token import Token

class Tokenizer:
    def tokenize(self, input_string, line):
        fsm = FiniteStateMachine()
        temp_tokens = []
        try:
            tokens = fsm.startMachine(input_string)
            for token in tokens:
                tokenObj = Token(
                    value=token.get("value"),
                    type=token.get("type"),
                    position=token.get("position"),
                    line=line
                )
                temp_tokens.append(tokenObj)
            return temp_tokens
        except TokenizationError as e:
            raise e 

    def readFile(self, path):
        lines = []
        with open(path, 'r') as file:
            for _, line in enumerate(file):
                if line.strip() != "":
                    lines.append(line)
        return lines
