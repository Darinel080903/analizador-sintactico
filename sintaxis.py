from ply import yacc
from lexer import tokens


def p_program(p):
    '''
    program : program declaration
            | declaration
    '''
    if len(p) == 2:  # solo una declaración
        p[0] = [p[1]]
    else:  # múltiples declaraciones
        p[1].append(p[2])
        p[0] = p[1]


def p_function_declaration(p):
    '''
    function_declaration : FUNCION ID OPERADOR_FLUJO LLAVE_IZQUIERDA program LLAVE_DERECHA
    | FUNCION ID CORRER OPERADOR_FLUJO LLAVE_IZQUIERDA program LLAVE_DERECHA
    '''
    p[0] = ('function_declaration', p[2], p[5])


def p_iterate_statement(p):
    '''
    iterate_statement : ITERAR NUMERO VECES OPERADOR_FLUJO expressionop
    '''
    p[0] = ('iterate_statement', p[2], p[5])


def p_operations(p):
    '''
    expressionop : expression MAS expression
               | expression MENOS expression
               | expression MAYOR_QUE expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_conditional_statement(p):
    '''
    conditional_statement : SI expression MAYOR_QUE expression REALIZA LLAVE_IZQUIERDA declaration LLAVE_DERECHA
    '''
    p[0] = ('conditional_statement', p[2], p[4], p[7])


def p_print_statement(p):
    '''
    print_statement : IMPRIMIR PARENTESIS_IZQUIERDO expression PARENTESIS_DERECHO PUNTO_Y_COMA
    '''
    p[0] = ('print_statement', p[3])


def p_declaration(p):
    '''
    declaration : variable_declaration
                | function_declaration
                | iterate_statement
                | print_statement
                | conditional_statement
                | call_function
                | expressionop
                | expressionop PUNTO_Y_COMA
    '''
    p[0] = p[1]


def p_call_function(p):
    '''
    call_function : OPERADOR_FLUJO ID PUNTO_Y_COMA
    '''
    p[0] = ('call_function', p[2])


def p_variable_declaration(p):
    '''
    variable_declaration : VARIABLE ID ASIGNACION expression PUNTO_Y_COMA
    '''
    p[0] = ('declaration', p[2], p[4])


def p_expression_number(p):
    '''
    expression : NUMERO
               | ID
    '''
    p[0] = p[1]


error_message = None


def p_error(p):
    global error_message
    if p is None:
        error_message = "Error de sintaxis: se ha alcanzado el final de la entrada y se esperaban más tokens."
    else:
        error_message = f"Error de sintaxis en el token '{p.type}' de valor '{p.value}'"


parser = yacc.yacc()
