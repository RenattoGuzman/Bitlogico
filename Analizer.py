import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = ['VARIABLE', 'CONSTANTE', 'NEGACION', 'CONJUNCION', 'DISYUNCION', 'IMPLICACION', 'EQUIVALENCIA', 'PARENTESIS_ABRE', 'PARENTESIS_CIERRA']

# Reglas léxicas
t_VARIABLE = r'[a-z]'
t_CONSTANTE = r'[01]'
t_NEGACION = r'~'
t_CONJUNCION = r'\^'
t_DISYUNCION = r'o'
t_IMPLICACION = r'=>'
t_EQUIVALENCIA = r'<=>'
t_PARENTESIS_ABRE = r'\('
t_PARENTESIS_CIERRA = r'\)'
t_ignore = ' \t'

# Reglas gramaticales
def p_formula(p):
    '''formula : VARIABLE
               | CONSTANTE
               | NEGACION formula
               | formula CONJUNCION formula
               | formula DISYUNCION formula
               | formula IMPLICACION formula
               | formula EQUIVALENCIA formula
               | PARENTESIS_ABRE formula PARENTESIS_CIERRA'''
    # Aquí se pueden realizar las acciones semánticas correspondientes
    pass

def p_error(p):
    print("Error de sintaxis")

# Construcción del analizador léxico
lexer = lex.lex()

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Ejemplo de entrada
entrada = "~(p ^ q) <=> (r o s)"

# Parsear la entrada
parser.parse(entrada)
