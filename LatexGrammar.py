from GrammaticFactory import GramaticsFactory
from Parser import Parser


rules = {
    "formula": {
        "rules": [
            ["constant"],
            ["proposition"],
            ["unaryFormula"],
            ["binaryFormula"]
        ]
    },
    "unaryFormula": {
        "rules": [
            ["openParenteses", "unaryOperator", "formula", "closeParenteses"]
        ]
    },
    "binaryFormula": {
        "rules": [
            ["openParenteses", "binaryOperator",
                "formula", "formula", "closeParenteses"]
        ]
    },
    "openParenteses": {
        "rules": [["("]]
    },
    "closeParenteses": {
        "rules": [[")"]]
    },
    "unaryOperator": {
        "rules": [["neg"]]
    },
    "binaryOperator": {
        "rules": [
            ["wedge"],
            ["vee"],
            ["rightarrow"],
            ["leftrightarrow"]
        ]
    },
    "constant": {
        "rules": [
            ["true"],
            ["false"]
        ]
    },
    "proposition": {
        "rules": [["propSymbol"]]
    }
}


factory = GramaticsFactory()

factory.newTerminals(['(', ')', 'neg', 'true', 'false', 'wedge',
                     'vee', 'rightarrow', 'leftrightarrow', 'propSymbol'])
factory.newNonTerminals(['formula', 'unaryFormula', 'openParenteses', 'closeParenteses',
                         'unaryOperator', 'binaryOperator', 'constant', 'proposition', 'binaryFormula'], initial='formula')

factory.newRules(rules)
LatexGrammar = factory.getGrammar()
LatexParser = Parser(gramatic=LatexGrammar)
