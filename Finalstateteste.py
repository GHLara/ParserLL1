class State:
    NEW_TOKEN = "NEW_TOKEN"
    PROPOSITION = "PROPOSITION"
    COMMAND = "COMMAND"
    OPEN_PARENTHESES = "OPEN_PARENTHESES"
    CLOSE_PARENTHESES = "CLOSE_PARENTHESES"
    CONSTANT = "CONSTANT"
    ERROR = "ERROR"


string = '(\\neg (((true))))(\\neg 1a)'

current_state = State.NEW_TOKEN
next_state = State.NEW_TOKEN
current_token = ""
char = ""
keywords = ["false", "true"]
commands = ["\\neg", "\\wedge", "\\vee", "\\rightarrow", "\\leftrightarrow"]
linebreak = [" ", "\n"]

# A função tem que receber um char e retornar um próximo estado
tokens = []


def tokenFind():
    global current_token
    global next_state

    tokens.append(current_token)
    current_token = ""
    next_state = State.NEW_TOKEN


def make_char_consumer(string):
    iterator = iter(string)

    def consumeChar():
        try:
            return next(iterator)
        except StopIteration:
            return None
    return consumeChar


def getCharType(char):
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
    else:
        return "unknown"


transition_table = {
    "digit":        {"next_state": State.PROPOSITION},
    "backslash":    {"next_state": State.COMMAND},
    "open_paren":   {"next_state": State.OPEN_PARENTHESES},
    "close_paren":  {"next_state": State.CLOSE_PARENTHESES},
    "bool_start":   {"next_state": State.CONSTANT},
    "whitespace":   {"next_state": State.NEW_TOKEN},
    "unknown":      {"next_state": State.ERROR},
}


def getNextState(type_char):
    transition = transition_table.get(type_char)
    return transition.get("next_state")


consumeChar = make_char_consumer(string)

while current_state != State.ERROR:

    if current_state == State.NEW_TOKEN:
        char = consumeChar()
        char_type = getCharType(char)
        print(getNextState(char_type))
        if char is None:
            break
        elif char.isdigit():
            current_token += char
            next_state = State.PROPOSITION
        elif char == "\\":
            current_token += char
            next_state = State.COMMAND
        elif char == "(":
            current_token += char
            next_state = State.OPEN_PARENTHESES
        elif char == ")":
            current_token += char
            next_state = State.CLOSE_PARENTHESES
        elif char == "t" or char == 'f':
            current_token += char
            next_state = State.CONSTANT
        elif char in linebreak:
            tokenFind()
            next_state = State.NEW_TOKEN
        else:
            current_token += char
            next_state = State.ERROR

    elif current_state == State.OPEN_PARENTHESES:
        tokenFind()

    elif current_state == State.CLOSE_PARENTHESES:
        tokenFind()

    elif current_state == State.CONSTANT:
        char = consumeChar()
        found_prefix = False

        for keyword in keywords:
            if keyword.startswith(current_token):
                current_token += char
                next_state = State.CONSTANT
                found_prefix = True
                if current_token == keyword:
                    tokenFind()
                    next_state = State.NEW_TOKEN
                break
        if not found_prefix:
            next_state = State.ERROR

    elif current_state == State.PROPOSITION:
        char = consumeChar()

        if char == None:
            break

        type_char = getCharType(char)

        if char.isalnum():
            current_token += char
            next_state = State.PROPOSITION
        elif type_char == 'close_paren':
            tokenFind()
            current_token += char
            next_state = getNextState(type_char)
        else:
            if len(current_token) > 1:
                tokenFind()
            else:
                next_state = State.ERROR

    elif current_state == State.COMMAND:
        char = consumeChar()
        found_prefix = False

        for keyword in commands:
            if keyword.startswith(current_token):
                current_token += char
                next_state = State.COMMAND
                found_prefix = True
                if current_token == keyword:
                    tokenFind()
                    next_state = State.NEW_TOKEN
                break
        if not found_prefix:
            next_state = State.ERROR
    current_state = next_state

# if current_state in {State.PROPOSITION, State.COMMAND, State.CONSTANT,
#                     State.OPEN_PARENTHESES, State.CLOSE_PARENTHESES} and current_token:
#     tokens.append(current_token)

if current_state == State.ERROR:
    print("Erro:", current_token)

else:
    print(tokens)
