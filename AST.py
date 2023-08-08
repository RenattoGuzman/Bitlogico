from graphviz import Digraph
class NodoAST:
    def __init__(self, value, left=None, right=None):
        self.valor = value
        self.izquierda = left
        self.derecha = right

# Función para mostrar el árbol utilizando Graphviz
def graficar_arbol(nodo):
    dot = Digraph(format='png')
    _graficar_arbol(dot, nodo)
    return dot

def _graficar_arbol(dot, nodo):
    if nodo:
        dot.node(str(id(nodo)), label=nodo.valor)
        if nodo.izquierda:
            dot.node(str(id(nodo.izquierda)), label=nodo.izquierda.valor)
            dot.edge(str(id(nodo)), str(id(nodo.izquierda)))
            _graficar_arbol(dot, nodo.izquierda)
        if nodo.derecha:
            dot.node(str(id(nodo.derecha)), label=nodo.derecha.valor)
            dot.edge(str(id(nodo)), str(id(nodo.derecha)))
            _graficar_arbol(dot, nodo.derecha)