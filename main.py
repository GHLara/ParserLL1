import os
from FSM.Tokenizer import Tokenizer
from LatexGrammar import LatexParser

def ReadFile(path: str):
    tokenizer = Tokenizer()
    with open(path, 'r') as file:
        for line_index, line in enumerate(file):
            tokenizer.tokenize(line, line_index)

    return tokenizer.tokens


if __name__ == "__main__":

    parser = LatexParser
    print(parser.table.getRule('formula', '('))

    '''
    path = "./inputs/"
    files = os.listdir(path)
    for index, file in enumerate(files):
        print(f"[{index}]" f" ({file})")

    fileIndex = input("Arquivo: ")
    findTokens = ReadFile(os.path.join(path, files[int(fileIndex)]))

    for token in findTokens:
        if not token.type == 'LINEBREAK':
            print(token.type, "=>", token.value)
    '''
