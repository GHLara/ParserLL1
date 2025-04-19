from Production import Production
from Symbol import Symbol
from typing import Dict


class Gramatics:
    _instance = None

    # Código padrão para criar um singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Gramatics, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.initial = None
        self.terminals: Dict[str, Production] = {}
        self.nonTerminals: Dict[str, Production] = {}
        self.mount()

    def Terminal(self, name: str) -> Production:
        sym = Symbol(name, isTerminal=True)
        self.terminals[name] = Production(sym)
        return self.terminals[name]

    def NonTerminal(self, name: str) -> Production:
        sym = Symbol(name, isTerminal=False)
        self.nonTerminals[name] = Production(sym)
        return self.nonTerminals[name]

    def showTerminals(self) -> None:
        for production in self.terminals.values():
            print(production.symbol.name)

    def showNonTerminals(self) -> None:

        for production in self.nonTerminals.values():
            print(production.symbol.name)

    def getProduction(self, name: str) -> Production:
        if name in self.terminals:
            return self.terminals[name]
        elif name in self.nonTerminals:
            return self.nonTerminals[name]
        else:
            return None

    def mount(self):

        # Constantes
        self.Terminal('true')
        self.Terminal('false')

        # Parenteses
        self.Terminal('(')
        self.Terminal(')')

        # Unario
        self.Terminal('neg')

        # Binario
        self.Terminal('wedge')
        self.Terminal('vee')
        self.Terminal('rightarrow')
        self.Terminal('leftrightarrow')

        # Proposicao
        self.Terminal('propSymbol')

        # self.showTerminals()

        self.NonTerminal('formula')
        self.NonTerminal('constant')
        self.NonTerminal('proposition')
        self.NonTerminal('unaryFormula')
        self.NonTerminal('binaryFormula')
        self.NonTerminal('openParenteses')
        self.NonTerminal('closeParenteses')
        self.NonTerminal('unaryOperator')
        self.NonTerminal('binaryOperator')

        self.getProduction('openParenteses').addProduction(
            [[self.terminals['(']]]
        )
        self.getProduction('closeParenteses').addProduction([
            [self.terminals[')']]
        ])

        self.getProduction('unaryOperator').addProduction(
            [[self.terminals['neg']]]
        )
        self.getProduction('binaryOperator').addProduction([
            [self.terminals['wedge']],
            [self.terminals['vee']],
            [self.terminals['rightarrow']],
            [self.terminals['leftrightarrow']]
        ])
        self.getProduction('constant').addProduction([
            [self.terminals['true']],
            [self.terminals['false']]
        ])
        self.getProduction('proposition').addProduction([
            [self.terminals['propSymbol']]
        ])

        self.getProduction('formula').addProduction(
            [
                [self.nonTerminals['constant']],
                [self.nonTerminals['proposition']],
                [self.nonTerminals['unaryFormula']],
                [self.nonTerminals['binaryFormula']]
            ]
        )

        self.getProduction('unaryFormula').addProduction(
            [
                [
                    self.nonTerminals['openParenteses'],
                    self.nonTerminals['unaryOperator'],
                    self.nonTerminals['formula'],
                    self.nonTerminals['closeParenteses'],
                ]
            ]
        )

        self.getProduction('binaryFormula').addProduction(
            [
                [
                    self.nonTerminals['openParenteses'],
                    self.nonTerminals['binaryOperator'],
                    self.nonTerminals['formula'],
                    self.nonTerminals['formula'],
                    self.nonTerminals['closeParenteses']
                ]
            ]
        )

        return self

# gramatics.getNonTerminal('formula').showRules()
# gramatics.getNonTerminal('constant').showRules()
# gramatics.getNonTerminal('proposition').showRules()
# gramatics.getNonTerminal('unaryFormula').showRules()
# gramatics.getNonTerminal('binaryFormula').showRules()
# gramatics.getNonTerminal('openParenteses').showRules()
# gramatics.getNonTerminal('closeParenteses').showRules()
# gramatics.getNonTerminal('unaryOperator').showRules()
# gramatics.getNonTerminal('binaryOperator').showRules()

# gramatics.showNonTerminals()

# print(gramatics.getNonTerminal('formula').getFirst())
