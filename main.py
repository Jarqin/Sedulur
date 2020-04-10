import sedulur_lexer
import sedulur_parser
import sedulur_interpreter

from sys import *

#DENGAN MASUKAN BAHASAKU.RHS
lexer = sedulur_lexer.BasicLexer()
parser = sedulur_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    sedulur_interpreter.BasicExecute(tree, env)
