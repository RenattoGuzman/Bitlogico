import ply.lex as lex
import ply.yacc as yacc
from AST import *
# Definición de tokens
tokens = ['VARIABLE', 'CONSTANTE', 'NEGACION', 'CONJUNCION', 'DISYUNCION', 'IMPLICACION', 'EQUIVALENCIA', 'PARENTESIS_ABRE', 'PARENTESIS_CIERRA']

# Reglas léxicas
t_VARIABLE = r'[a-z]'
t_CONSTANTE = r'[0-1]'
t_NEGACION = r'~'
t_CONJUNCION = r'\^'
t_DISYUNCION = r'o'
t_IMPLICACION = r'=>'
t_EQUIVALENCIA = r'<=>'
t_PARENTESIS_ABRE = r'\('
t_PARENTESIS_CIERRA = r'\)'
t_ignore = ' \t'

# Reglas gramaticales segun caso para construccion del arbol
def p_negacion(p):
    '''
    formula : NEGACION formula
    '''
    #crear el nodo en la expresion p
    nodo = NodoAST(p[1]) #simbolo
    nodo.derecha = p[2] #valor
    p[0] = nodo 
def p_agrupacion(p): #expresiones agrupadas
    '''
    formula : PARENTESIS_ABRE formula PARENTESIS_CIERRA
    '''
    p[0] = p[2]#obtener el valor entre los parentesis

def p_formula_valor(p): #variable o constante
    '''
    formula : VARIABLE
               | CONSTANTE
    '''
    p[0] = NodoAST( p[1] )

def p_formula(p):
    '''formula :
               | formula CONJUNCION formula
               | formula DISYUNCION formula
               | formula IMPLICACION formula
               | formula EQUIVALENCIA formula'''
    # Aquí se pueden realizar las acciones semánticas correspondientes
    # Crear un nodo para el operador
    nodo = NodoAST(p[2])  # p[2] contiene el operador
    nodo.izquierda = p[1]  # p[1] contiene el nodo izquierdo
    nodo.derecha = p[3]  # p[3] contiene el nodo derecho
    p[0] = nodo


def t_error(t):
    print(f'caracter no valido: {t[0]}')
    t.lexer.skip(1)
def p_error(p):
    print("Error de sintaxis")

# Construcción del analizador léxico
lexer = lex.lex()

#definir precedencias para el arbol
precedence = (
    ('left', 'IMPLICACION', 'EQUIVALENCIA'),
    ('left', 'DISYUNCION'),
    ('left', 'CONJUNCION'),
    ('left', 'NEGACION')
)

# Construcción del analizador sintáctico
parser = yacc.yacc()

def verificar_expresion(expresion):
        r_arbol = parser.parse(expresion, lexer = lexer) 
        if(r_arbol):
            png = graficar_arbol(r_arbol)
            png.view(filename=f'output')
            print(f"Análisis sintáctico exitoso. La expresión {expresion} es bien formulada.")
        else:
             print(f"La expresión {expresion} no está bien formulada.")


verificar_expresion("(p<=>~p)")