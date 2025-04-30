from Production import Production
from Symbol import Symbol
from typing import Dict


class Gramatics:
    def __init__(self):
        self.initial = None
        self.terminals: Dict[str, Production] = {}
        self.nonTerminals: Dict[str, Production] = {}

    def Terminal(self, name: str) -> Production:
        sym = Symbol(name, isTerminal=True)
        self.terminals[name] = Production(sym)
        return self.terminals[name]

    def NonTerminal(self, name: str, isInitial=False) -> Production:
        sym = Symbol(name, isTerminal=False, isInitial=isInitial)
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
