import ply.lex as lex

# Palabras reservadas
reserved = {
    'iterar': 'ITERAR',
    'veces': 'VECES',
    'variable': 'VARIABLE',
    'funcion': 'FUNCION',
    'correr': 'CORRER',
    'imprimir': 'IMPRIMIR',
    'si': 'SI', 
    'realiza': 'REALIZA',  
}

# Lista de tokens
tokens = [
    'ID',
    'NUMERO',
    'ASIGNACION',
    'PUNTO_Y_COMA',
    'OPERADOR_FLUJO',
    'MAS',
    'MENOS',  # Asegúrate de tener un token para el signo -
    'MAYOR_QUE',  # Token para el operador >
    'LLAVE_IZQUIERDA',
    'LLAVE_DERECHA',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
    'MENOR_QUE'
] + list(reserved.values())

# Reglas simples para tokens

t_ASIGNACION = r'='
t_PUNTO_Y_COMA = r';'
t_OPERADOR_FLUJO = r'>>'
t_MAS = r'\+'
t_MENOS = r'-'
t_MAYOR_QUE = r'>'
t_LLAVE_IZQUIERDA = r'\{'
t_LLAVE_DERECHA = r'\}'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_MENOR_QUE = r'<'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    global error_message
    error_message = f"Error de sintaxis: Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}"
    t.lexer.skip(1)

lexer = lex.lex()
