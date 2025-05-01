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
    "formulaContainer": {
        "rules": [
            ["unaryFormula"],
            ["binaryFormula"]
        ]
    },
    "parentesesContainer": {
        "rules": [
            ["openParenteses", "formulaContainer", "closeParenteses"],
        ]
    },
    "unaryFormula": {
        "rules": [
            ["unaryOperator", "formula"]
        ]
    },
    "binaryFormula": {
        "rules": [
            ["binaryOperator", "formula", "formula"]
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

factory.newNonTerminals(['formula','formulaContainer', 'parentesesContainer', 'unaryFormula', 'openParenteses', 'closeParenteses',
                         'unaryOperator', 'binaryOperator', 'constant', 'proposition', 'binaryFormula'], initial='formula')

factory.newRules(rules)
LatexGrammar = factory.getGrammar()
LatexParser = Parser(gramatic=LatexGrammar)
