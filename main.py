from Parser import Parser
import os
from FSM.Tokenizer import Tokenizer
from LatexGrammar import LatexGrammar


if __name__ == "__main__":
    path = "./inputs/"
    files = os.listdir(path)
    for index, file in enumerate(files):
        print(f"[{index}]" f" ({file})")
    
    fileIndex = input("Arquivo: ")
    filePath = os.path.join(path, files[int(fileIndex)])

    #Vamos extrair os tokens do arquivo
    tokenizer = Tokenizer()
    tokenizer.readFile(filePath)

    #Agora, podemos chamar nosso Parser, passando nossa gramática e nossos tokens.
    LatexParser = Parser(gramatic=LatexGrammar, tokens=tokenizer.tokens)
    LatexParser.view()
