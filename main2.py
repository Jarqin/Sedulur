import sedulur_lexer
import sedulur_parser
import sedulur_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = sedulur_lexer.BasicLexer()
    parser = sedulur_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('sedulur > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            sedulur_interpreter.BasicExecute(tree, env)