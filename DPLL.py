def DPLL(B, I):
    if not B:  # Si no hay cláusulas restantes, la fórmula es satisfacible
        return True, I
    
    for clause in B:
        if not clause:  # Si alguna cláusula está vacía, la fórmula no es satisfacible
            return False, None
    
    # Seleccionar una literal L (aquí se selecciona el primer literal de la primera cláusula)
    L = next(iter(B[0]))

    # Crear B' eliminando cláusulas con L y complementos de L
    B_true = [clause - {-L} for clause in B if L in clause]
    
    # Crear B'' eliminando cláusulas con complemento de L y L
    B_false = [clause - {L} for clause in B if -L in clause]

    # Verificar que el tamaño de B disminuya en cada llamada recursiva
    if len(B_true) >= len(B) or len(B_false) >= len(B):
        return False, None

    # Asignar L como verdadero en la asignación parcial I
    I_true = I.copy()
    I_true[abs(L)] = True

    # Llamada recursiva con L verdadero
    result_true, assignment_true = DPLL(B_true, I_true)
    if result_true:
        return True, assignment_true

    # Asignar L como falso en la asignación parcial I
    I_false = I.copy()
    I_false[abs(L)] = False

    # Llamada recursiva con L falso
    result_false, assignment_false = DPLL(B_false, I_false)
    if result_false:
        return True, assignment_false

    return False, None

# Ejemplo de uso
if __name__ == "__main__":
    # Representación de la fórmula en forma de cláusulas (conjuntos de literales)
    B = [
        {1},   # Variable 1 representa "p"
        {-1}   # Complemento de variable 1 representa "-p"
    ]
    I = {}

    result, assignment = DPLL(B, I)

    if result:
        print("La fórmula es satisfacible. Asignación parcial:", assignment)
    else:
        print("La fórmula no es satisfacible.")
