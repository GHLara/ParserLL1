from FSM.Token import Token


class State:
    NEW_TOKEN = "NEW_TOKEN"
    PROPOSITION = "PROPOSITION"
    COMMAND = "COMMAND"
    OPEN_PARENTHESES = "OPEN_PARENTHESES"
    CLOSE_PARENTHESES = "CLOSE_PARENTHESES"
    CONSTANT = "CONSTANT"
    LINEBREAK = "LINEBREAK"
    ERROR = "ERROR"
    END = "END"


transition_table = {
    "close_paren": State.CLOSE_PARENTHESES,
    "open_paren":  State.OPEN_PARENTHESES,
    "bool_start":  State.CONSTANT,
    "whitespace":  State.LINEBREAK,
    "backslash":   State.COMMAND,
    "digit":       State.PROPOSITION,
}

keywords = ["false", "true"]
commands = ["\\neg", "\\wedge", "\\vee", "\\rightarrow", "\\leftrightarrow"]
linebreak = [" ", "\n"]


class TokenizationError(Exception):
    def __init__(self, message, expected=None, column=None, token=None):
        super().__init__(message)
        self.expected = expected
        self.column = column
        self.token = token

    def __str__(self):
        base = super().__str__()
        return f"{base} (Expected: {self.expected}, Received: {self.token}, At: {self.column})"


class FiniteStateMachine:
    def __init__(self):
        self.current_state = State.NEW_TOKEN
        self.next_state = State.NEW_TOKEN
        self.current_token = ""
        self.tokens = []
        self.consumeChar = None
        self.getCharIndex = None

    def make_char_consumer(self, string):
        iterator = iter(string)
        index = -1

        def consumeChar():
            nonlocal index
            try:
                index += 1
                return next(iterator)
            except StopIteration:
                return None

        def get_index():
            return index

        self.getCharIndex = get_index
        self.consumeChar = consumeChar

    def getNextState(self, type_char):
        return transition_table.get(type_char)

    def saveToken(self):
        token = {
            "value": self.current_token,
            "type": self.current_state,
            "position": self.getCharIndex()
        }

        self.tokens.append(token)
        self.current_token = ""
        self.next_state = State.NEW_TOKEN

    def getCharType(self, char):
        if char == None:
            return "unknown"
        elif char.isdigit():
            return "digit"
        elif char == "\\":
            return "backslash"
        elif char == "(":
            return "open_paren"
        elif char == ")":
            return "close_paren"
        elif char in ("t", "f"):
            return "bool_start"
        elif char in (" ", "\n", "\t"):
            return "whitespace"
        elif char.isalnum():
            return "alnum"
        else:
            return "unknown"

    def startMachine(self, input_string: str):
        self.make_char_consumer(input_string)

        while self.current_state != State.END:
            if self.current_state == State.NEW_TOKEN:
                char = self.consumeChar()

                if char is None:
                    self.current_state = State.END
                    break

                char_type = self.getCharType(char)
                self.current_token += char
                self.next_state = self.getNextState(char_type)

            elif self.current_state == State.OPEN_PARENTHESES:
                self.saveToken()

            elif self.current_state == State.CLOSE_PARENTHESES:
                self.saveToken()

            elif self.current_state == State.LINEBREAK:
                self.saveToken()

            elif self.current_state == State.CONSTANT:
                char = self.consumeChar()
                found_prefix = False

                for keyword in keywords:
                    if keyword.startswith(self.current_token):
                        self.current_token += char
                        self.next_state = State.CONSTANT
                        found_prefix = True
                        if self.current_token == keyword:
                            self.saveToken()
                        break
                if not found_prefix:
                    raise TokenizationError(
                        "Token invalido identificado",
                        column=self.getCharIndex(),
                        token=self.current_token,
                        expected=self.current_state
                    )

            elif self.current_state == State.PROPOSITION:
                char = self.consumeChar()

                if char == None:
                    self.saveToken()
                    break

                type_char = self.getCharType(char)

                if type_char == "alnum" or type_char == 'digit':
                    self.current_token += char
                    self.next_state = State.PROPOSITION
                elif type_char == 'close_paren':
                    self.saveToken()
                    self.current_token += char
                    self.next_state = self.getNextState(type_char)
                elif type_char == "whitespace":
                    self.saveToken()
                    self.current_token += char
                    self.next_state = self.getNextState(type_char)
                else:
                    self.current_token += char
                    raise TokenizationError(
                        "Token invalido identificado",
                        column=self.getCharIndex() + 1,
                        token=self.current_token,
                        expected=self.current_state
                    )

            elif self.current_state == State.COMMAND:
                char = self.consumeChar()
                found_prefix = False

                for keyword in commands:
                    if keyword.startswith(self.current_token):
                        self.current_token += char
                        self.next_state = State.COMMAND
                        found_prefix = True
                        if self.current_token == keyword:
                            self.saveToken()
                        break
                if not found_prefix:
                    raise TokenizationError(
                        "Token invalido identificado",
                        column=self.getCharIndex(),
                        token=self.current_token,
                        expected=self.current_state
                    )
            self.current_state = self.next_state
        self.current_state = State.NEW_TOKEN
        return self.tokens
