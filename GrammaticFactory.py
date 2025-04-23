from Gramatics import Gramatics

class GramaticsFactory:
    def __init__(self):
        self.grammar = Gramatics()

    def newTerminals(self, terminals: list[str]):
        for terminal in terminals:
            self.grammar.Terminal(terminal)

    def newNonTerminals(self, nonTerminals: list[str], initial=str):
        for nonTerminal in nonTerminals:
            self.grammar.NonTerminal(nonTerminal, nonTerminal == initial)

    def newRules(self, rules: dict):
        for head, rule_data in rules.items():
            production = self.grammar.getProduction(head)

            if production is None:
                raise ValueError(
                    f"Não foi encontrada uma produção para '{head}'.")

            for alt in rule_data["rules"]:
                symbols = []
                for sym in alt:
                    if sym in self.grammar.terminals:
                        symbols.append(self.grammar.terminals[sym])
                    elif sym in self.grammar.nonTerminals:
                        symbols.append(self.grammar.nonTerminals[sym])
                    else:
                        raise ValueError(
                            f"Símbolo '{sym}' não foi declarado como terminal ou não-terminal.")
                production.addProduction([symbols])

    def getGrammar(self):
        return self.grammar



