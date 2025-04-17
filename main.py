import os
from Tokenizer import Tokenizer


def ReadFile(path: str):
    tokenizer = Tokenizer()

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                tokens = tokenizer.TokenExtractor(line)
                print(f"File: {path}, Tokens: {tokens}")


if __name__ == "__main__":
    path = "./inputs/"
    files = os.listdir(path)

    for file in files:
        ReadFile(os.path.join(path, file))
