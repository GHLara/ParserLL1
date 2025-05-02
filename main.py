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
    LatexParser = Parser(gramatic=LatexGrammar)

    tokenizer = Tokenizer()
    lines = tokenizer.readFile(filePath)
    for index, line in enumerate(lines):
        if(index > 0 and line.strip() != ""):        
            try:
                tokens = tokenizer.tokenize(line, index)
                LatexParser.parse(tokens)
                print(''.join([x.value for x in tokens if x.value != '\n']), '-> Válido')
            except Exception as e:
                print(line.replace('\n', ''), '-> Inválido')

