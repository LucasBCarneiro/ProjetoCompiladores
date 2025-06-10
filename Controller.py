from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer
from SymbolTable import SymbolTable
from LexTable import LexTable

import os
import sys

def get_file():
    args = sys.argv

    if len(args) > 1:
        return args[1]
    else:
        print(os.path.abspath(os.getcwd()))
        print('Nao obtive arquivo, entao iremos usar o padrao: {}'.format(os.path.abspath(os.getcwd()) + '/txts/teste.DKS'))
        return os.path.abspath(os.getcwd()) + '/txts/teste.DKS'

if __name__ == '__main__':
    filepath = get_file()
    Buffer = Buffer(filepath)
    Analyzer = LexicalAnalyzer()

    # Lista de todos os valores retornados da funcao de tokenizar
    token = []
    lexeme = []
    row = []
    column = []

    # Tokenizar e recarregar o buffer
    for i in Buffer.load_buffer():
        t, lex, lin, col = Analyzer.tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col

    print('\nTokens reconhecidos: ', token)


    SymbolTable = SymbolTable(token, lexeme, row, filepath)
    LexTable = LexTable(token, lexeme, filepath)



