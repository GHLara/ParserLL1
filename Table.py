class Table:

    def __init__(self):

        self.table = {}
        self.rows = []
        self.columns = []
        self.max = 0

    def mount(self, parser, gramatic):

        for terminal in gramatic.terminals.values():
            self.columns.append(terminal.symbol.name)

        #Para cada não terminal
        for nonTerminal in gramatic.nonTerminals.values():

            self.rows.append(nonTerminal.symbol.name)
            self.table[nonTerminal.symbol.name] = {}

            #Para cada símbolo não terminal
            for symbol in parser.getFirst(nonTerminal.symbol.name):

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

                    if has_symbol:
                        self.table[nonTerminal.symbol.name][symbol] = rule

        self.showTable()
    
    def getRule(self, symbol1, symbol2):
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
                    f.write(f"{valor:>32}")
                f.write("\n")
