from typing import List
from Symbol import Symbol

class Production:
    def __init__(self, symbol: Symbol):
        self.symbol = symbol
        self.productions: List[Production] = []
        self.first = []
        self.follow = []

    def addProduction(self, production_list):
        for production in production_list:
            self.productions.append(production)
    
    def showRules(self):
        rulesStr = f"{self.symbol.name} ="
        first = True

        for rule in self.productions:            
            symbols = ""
            for production in rule:
                symbols += production.symbol.name + " "
            if first:
                rulesStr += f" {symbols}"
            else:
                rulesStr += f" | {symbols}"
            
            first = False
        
        print(rulesStr)
