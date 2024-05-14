import ply.lex as lex

# Lista de tokens
tokens = [
    'ID',
    'NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ASSIGN',
    'IF',
    'THEN',
    'ELSE',
    'END',
    'WHILE',
    'DO'
]

# Definir expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_ASSIGN = r':='
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_END = r'end'
t_WHILE = r'while'
t_DO = r'do'

# Regla para el token ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

# Regla para el token NUM
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores de caracteres ilegales
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función para probar el lexer con una cadena de entrada proporcionada por el usuario
def probar_lexer():
    print("Bienvenido al analizador léxico de Tiny.")
    print("Ingrese el código de entrada línea por línea. Presione Enter en una línea vacía para finalizar.")
    lineas = []
    while True:
        linea = input()
        if not linea:
            break
        lineas.append(linea)
    data = '\n'.join(lineas)

    # Reemplazar identificadores por 'ID' en la entrada
    for token in tokens:
        data = data.replace(token.lower(), token)

    # Imprimir la entrada modificada
    print("\nEntrada modificada:")
    print(data)

    lexer.input(data)
    print("\nTokens encontrados:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Ejecutar el analizador léxico
if __name__ == "__main__":
    probar_lexer()
