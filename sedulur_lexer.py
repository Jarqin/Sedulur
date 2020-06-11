from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, PRINT, IF, ELSE, THEN, EQEQ, FOR, TO }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    PRINT = r'CETA'
    IF = r'MENAWI'
    ELSE = f'LAEN'
    THEN = r'DUDI'
    FOR = r'PIKEUN'
    TO = r'BANJUR'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('sedulur > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)