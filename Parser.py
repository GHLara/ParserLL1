from Production import Production
from Gramatics import Gramatics


class Parser:
    def __init__(self):
        self.gramatic = Gramatics()

    def defineFirst(self, initialProduction: Production):
        if len(initialProduction.productions) == 0:
            if (initialProduction.symbol.isTerminal):
                print(
                    f"Terminal symbol '{initialProduction.symbol.name}' has not first")
            else:
                print(
                    f"Production rules not defined for: {initialProduction.symbol.name}")
            return []

        for rule in initialProduction.productions:
            for production in rule:
                if production.symbol.isTerminal:
                    if production.symbol.name not in initialProduction.first:
                        initialProduction.first.append(production.symbol.name)
                    break

                else:
                    for symbol in self.getFirst(production.symbol.name):
                        if symbol not in initialProduction.first:
                            initialProduction.first.append(symbol)
                    break

        return initialProduction.first

    def getFirst(self, symbolStr):
        production = self.gramatic.getProduction(symbolStr)

        if len(production.first) > 0:
            return production.first

        return self.defineFirst(production)

    def getFollow(self, symbolStr):

        production = self.gramatic.getProduction(symbolStr)
        if len(production.follow) > 0:
            return production.follow

        return self.defineFollow(production)

    def defineFollow(self, intial_production):

        rules_list = []

        for rules in self.gramatic.nonTerminals.values():
            for rule in rules.productions:
                for production in rule:
                    if production.symbol.name == intial_production.symbol.name:
                        rules_list.append(rules.symbol.name )

        print(rules_list)



parser = Parser()

print(parser.getFollow('formula'))
