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
    "unknown":     State.ERROR,
    "digit":       State.PROPOSITION,
}


def make_char_consumer(string):
    iterator = iter(string)

    def consumeChar():
        try:
            return next(iterator)
        except StopIteration:
            return None
    return consumeChar


string = r'''
true
false
1a
2xyz
(\neg true)(\neg 1a)
(\wedge true false)
'''

current_state = State.NEW_TOKEN
next_state = State.NEW_TOKEN
current_token = ""

consumeChar = make_char_consumer(string)

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


def getNextState(type_char):
    return transition_table.get(type_char)


while current_state != State.END:
    if current_state == State.NEW_TOKEN:
        char = consumeChar()

        if char is None:
            current_state = State.END
            break

        char_type = getCharType(char)
        current_token += char
        next_state = getNextState(char_type)

    elif current_state == State.OPEN_PARENTHESES:
        tokenFind()

    elif current_state == State.CLOSE_PARENTHESES:
        tokenFind()

    elif current_state == State.LINEBREAK:
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

if current_state == State.ERROR:
    print("Erro:", current_token)

else:
    print("Token Final:", current_token)
    print("Estado Final:", current_state)
    print(tokens)
