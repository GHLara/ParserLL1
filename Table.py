from Gramatics import Gramatics
from GrammaticFactory import GramaticsFactory
from constants import CIFRAO
from LatexGrammar import LatexParser, LatexGrammar

class Table:

    def __init__(self, gramatic: Gramatics):

        self.gramatic = gramatic
        self.table = {}
        self.rows = []
        self.columns = []
        self.max = 0

    def mount(self):

        for terminal in self.gramatic.terminals.values():
            self.columns.append(terminal.symbol.name)

        #Para cada não terminal
        for nonTerminal in self.gramatic.nonTerminals.values():

            self.rows.append(nonTerminal.symbol.name)
            self.table[nonTerminal.symbol.name] = {}

            #Para cada símbolo não terminal
            for symbol in nonTerminal.first:

                #Para cada regra de produção
                for production_list in nonTerminal.productions:

                    regra = ""
                    has_symbol = False
                    #Para cada saída de regra
                    for production in production_list:

                        rule = f"{nonTerminal.symbol.name} -> {production.symbol.name}"
                        
                        if(len(rule) > self.max):
                            self.max = len(rule)

                        if symbol in production.first:
                            has_symbol = True
                        
                        elif symbol == production.symbol.name:
                            has_symbol = True

                    print(rule)

                    if has_symbol:
                        self.table[nonTerminal.symbol.name][symbol] = rule

        self.showTable()

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
                    f.write(f"{valor:>32}")
                f.write("\n")


table = Table(LatexGrammar)
parser = LatexParser
print(parser.getFirst('formula'))

table.mount()

for nonTerminal in table.gramatic.nonTerminals:
    print(f"{nonTerminal} => First {parser.getFirst(nonTerminal)}")
