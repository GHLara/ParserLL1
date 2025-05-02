from GrammaticFactory import GramaticsFactory

# Rules deve ser um array.
# Multiplos arrays dentro de Rules representam um OU
# Valores dentro de cada array representam um E
# A ou B = [['A']['B']]
# A e B = [['A', 'B']]

rules = {
    "FORMULA": {
        "rules": [
            ["CONSTANT"],
            ["PROPOSITION"],
            ["PARENTHESES_CONTAINER"]
        ]
    },
    "FORMULA_CONTAINER": {
        "rules": [
            ["PARENTHESES_CONTAINER"],
            ["UNARY_FORMULA"],
            ["BINARY_FORMULA"]
        ]
    },
    "PARENTHESES_CONTAINER": {
        "rules": [
            ["OPEN_PARENTHESES", "FORMULA_CONTAINER", "CLOSE_PARENTHESES"],
        ]
    },
    "UNARY_FORMULA": {
        "rules": [
            ["UNARY_OPERATOR", "FORMULA"]
        ]
    },
    "BINARY_FORMULA": {
        "rules": [
            ["BINARY_OPERATOR", "FORMULA", "FORMULA"]
        ]
    },
    "OPEN_PARENTHESES": {
        "rules": [["("]]
    },
    "CLOSE_PARENTHESES": {
        "rules": [[")"]]
    },
    "UNARY_OPERATOR": {
        "rules": [["\\neg"]]
    },
    "BINARY_OPERATOR": {
        "rules": [
            ["\\wedge"],
            ["\\vee"],
            ["\\rightarrow"],
            ["\\leftrightarrow"]
        ]
    },
    "CONSTANT": {
        "rules": [
            ["true"],
            ["false"]
        ]
    },
    "PROPOSITION": {
        "rules": [["PROP_SYMBOL"]]
    }
}


factory = GramaticsFactory()

factory.newTerminals(['(', ')', '\\neg', 'true', 'false', '\\wedge',
                     '\\vee', '\\rightarrow', '\\leftrightarrow', 'PROP_SYMBOL'])

factory.newNonTerminals(['FORMULA', 'FORMULA_CONTAINER', 'PARENTHESES_CONTAINER', 'UNARY_FORMULA', 'BINARY_FORMULA', 'OPEN_PARENTHESES', 'CLOSE_PARENTHESES',
                         'UNARY_OPERATOR', 'BINARY_OPERATOR', 'CONSTANT', 'PROPOSITION'], initial='FORMULA')

factory.newRules(rules)
LatexGrammar = factory.getGrammar()
