import re
from Constants import CONSTANTE, PROPOSICAO, ABREPAREN, FECHAPAREN, OPERADORUNARIO, OPERADORBINARIO, WHITESPACE


class Tokenizer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.patterns = {
                'CONSTANTE': re.compile(CONSTANTE),
                'PROPOSICAO': re.compile(PROPOSICAO),
                'ABREPAREN': re.compile(ABREPAREN),
                'FECHAPAREN': re.compile(FECHAPAREN),
                'OPERADORUNARIO': re.compile(OPERADORUNARIO),
                'OPERADORBINARIO': re.compile(OPERADORBINARIO),
                'WHITESPACE': re.compile(WHITESPACE),
            }
        return cls._instance

    def TokenExtractor(self, text: str):
        tokens = []
        for token_type, pattern in self.patterns.items():
            match = pattern.search(text)
            if match:
                tokens.append((token_type, match.group()))
        return tokens
