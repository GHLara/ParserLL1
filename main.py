import os
from Tokenizer import Tokenizer


def ReadFile(path: str):
    tokenizer = Tokenizer()
    with open(path, 'r') as file:
        for line_index, line in enumerate(file):
            tokenizer.tokenize(line, line_index)


if __name__ == "__main__":
    path = "./inputs/"
    files = os.listdir(path)
    for file in files:
        ReadFile(os.path.join(path, file))
