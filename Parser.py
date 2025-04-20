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
        if(production == None):
            print(f"Production rule not defined for {symbolStr}")
            return None
        
        if(production.symbol.isInitial):
            if len(production.follow) == 0:
                production.follow.append('$')
                return self.defineFollow(production)

        if len(production.follow) > 0:
            return production.follow

        return self.defineFollow(production)

    def defineFollow(self, intial_production):
        # percorre todos os não terminais
        for rules in self.gramatic.nonTerminals.values():
            # percorre todas as regras do não terminal
            for rule in rules.productions:
                production_index = 0
                # percorre cada elemento de cada regra
                for production in rule:
                    production_index += 1

                    if production.symbol.name == intial_production.symbol.name:
                        
                        if(production_index < len(rule)):
                            for follow_symbol in self.getFirst(rule[production_index].symbol.name):
                                if(follow_symbol not in intial_production.follow):
                                    intial_production.follow.append(follow_symbol)

                        else:
                            for follow_symbol in self.getFollow(rules.symbol.name):
                                if(follow_symbol not in intial_production.follow):
                                    intial_production.follow.append(follow_symbol)
        
        print(intial_production.follow)
        return intial_production.follow

parser = Parser()
parser.getFollow('openParenteses')



