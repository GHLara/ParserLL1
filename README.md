# ParserLL1

# Validador de Expressões de Lógica Proposicional em LaTeX

Este projeto consiste em um analisador léxico e um parser LL(1) desenvolvido para validar expressões de lógica proposicional escritas em LaTeX. O objetivo é verificar se as expressões estão **lexical e gramaticalmente corretas**, considerando apenas a **forma** da expressão, não seu conteúdo lógico.

## ✨ Funcionalidades

- Analisador léxico que simula uma **máquina de estados finitos**;
- Analisador sintático **LL(1)** para validar a gramática das expressões;
- Leitura das expressões a partir de um **arquivo texto** fornecido via linha de comando;
- Saída no terminal indicando se cada expressão é **"valida"** ou **"inválida"**.

## 📥 Formato da Entrada

O arquivo de entrada deve seguir o seguinte padrão:

```
N
expressão_1
expressão_2
...
expressão_N
```

- `N`: número inteiro indicando a quantidade de expressões a serem validadas.
- Cada `expressão_i` é uma linha contendo uma expressão lógica em LaTeX.

## 📤 Formato da Saída

Para cada expressão do arquivo de entrada, o programa imprimirá no terminal:

- `valida` se a expressão estiver correta;
- `inválida` caso contrário.

## 🚀 Execução

Execute o programa via linha de comando, passando o caminho do arquivo como argumento:

## 🛠 Tecnologias

- Linguagem: [Python](https://www.python.org/)
- Simulação de autômato finito e parser LL(1).

## 📚 Objetivo Acadêmico

Este projeto foi desenvolvido como parte da disciplina de **Construção de Interpretadores** da **Pontificia Universidade Católica do Paraná**, ministrada por **Frank Coelho de Alcantara**.
