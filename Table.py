from Production import Production
from Gramatics import Gramatics
from constants import CIFRAO

class Table:

    def __init__(self, gramatic: Gramatics):

        self.table = {}
        self.rows = []
        self.columns = []
        self.gramatic = gramatic
        self.mount()

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

                        if (production_index < len(rule)):
                            for follow_symbol in self.getFirst(rule[production_index].symbol.name):
                                if (follow_symbol not in intial_production.follow):
                                    intial_production.follow.append(
                                        follow_symbol)

                        else:
                            for follow_symbol in self.getFollow(rules.symbol.name):
                                if (follow_symbol not in intial_production.follow):
                                    intial_production.follow.append(
                                        follow_symbol)

        print(intial_production.follow)
        return intial_production.follow

    def getFollow(self, symbolStr):

        production = self.gramatic.getProduction(symbolStr)
        if (production == None):
            print(f"Production rule not defined for {symbolStr}")
            return None

        if (production.symbol.isInitial):
            if len(production.follow) == 0:
                production.follow.append(CIFRAO)
                return self.defineFollow(production)

        if len(production.follow) > 0:
            return production.follow

        return self.defineFollow(production)

    def mount(self):

        for terminal in self.gramatic.terminals.values():
            self.columns.append(terminal.symbol.name)

        #Para cada não terminal
        for nonTerminal in self.gramatic.nonTerminals.values():

            self.rows.append(nonTerminal.symbol.name)
            self.table[nonTerminal.symbol.name] = {}

            #Para cada símbolo não terminal
            for symbol in self.getFirst(nonTerminal.symbol.name):

                #Para cada regra de produção
                for production_list in nonTerminal.productions:

                    has_symbol = False
                    rule = []
                    #Para cada saída de regra
                    for production in production_list:

                        rule.append(production.symbol.name)

                        if symbol in production.first:
                            has_symbol = True
                        
                        elif symbol == production.symbol.name:
                            has_symbol = True

                    if has_symbol:
                        self.table[nonTerminal.symbol.name][symbol] = rule

        #self.showTable()
    
    def getRule(self, symbol1, symbol2):
        if symbol1 not in self.table:
            return None
            
        if symbol2 not in self.table[symbol1]:
            return None
            
        return self.table[symbol1][symbol2]

    def showTable(self):
        
        with open("matriz_formatada.txt", "w", encoding="utf-8") as f:

            f.write(f"{'':>32}")
            for col in self.columns:
                f.write(f"{col:>32}")
            f.write("\n")

            for x in self.rows:
                f.write(f"{x:>32}")
                for y in self.columns:
                    valor = self.table.get(x, {}).get(y, 0)
                    f.write(f"{valor}")
                f.write("\n")
