# Usei esse cara como referência: https://www.codementor.io/@arpitbhayani/building-finite-state-machines-with-python-coroutines-15nk03eh9l

class FSM:
    _instance = None

    # Código padrão para criar um singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FSM, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Os estados finais da minha máquina de estados, toda vez que chegar em um deles, o estado é resetado.
        self.final_states = {
            ' ': 'whitespace',
            '\n': 'whitespace',
            '(': 'parenteses',
            ')': 'parenteses',
            'true': 'Constante',
            'false': 'Constante',
            '\\neg': 'unario',
            '\\wedge': 'binario',
            '\\vee': 'binario',
            '\\rightarrow': 'binario',
            '\\leftrightarrow': 'binario'
        }
        self.token_list = []
        self.state = ""
        self.initialized = True
        self.matcher = self.process_input()
        self.startMatcher()

    # Função principal da classe
    def process_input(self):
        while True:
            char: str = (yield)

            if char in self.final_states:
                if self.state:
                    self.process_state()
                    self.state = ""
                self.state = char
                self.process_state()
                self.state = ""
            else:
                self.state += char

    def process_state(self):
        token_type = self.final_states.get(self.state)

        if token_type:
            self.token_list.append((self.state, token_type))
            return True

        # Não consigo definir a proposição sem uma função de validação.
        elif self.is_proposicao():
            self.token_list.append((self.state, 'proposicao'))
            return True

        else:
            return False

    def is_proposicao(self):
        if not self.state[0].isdigit():
            return False

        return all(c.isdigit() or c.islower() for c in self.state[1:])

    # Função para startar a corrotina
    def startMatcher(self):
        next(self.matcher)

    # Ler string
    def send(self, str):
        for char in str:
            self.matcher.send(char)
