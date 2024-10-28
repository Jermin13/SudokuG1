import random

# Crear un tablero vacío de sudoku
def crear_tablero():
    return [[0 for _ in range(9)] for _ in range(9)]

# Imprimir el tablero en formato amigable
def imprimir_tablero(tablero):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()
    print()

# Verificar si un número es válido en la posición dada
def es_valido(tablero, num, fila, col):
    # Revisar la fila
    if num in tablero[fila]:
        return False
    # Revisar la columna
    if num in [tablero[i][col] for i in range(9)]:
        return False
    # Revisar la caja 3x3
    caja_fila = (fila // 3) * 3
    caja_col = (col // 3) * 3
    for i in range(caja_fila, caja_fila + 3):
        for j in range(caja_col, caja_col + 3):
            if tablero[i][j] == num:
                return False
    return True

# Resolver el sudoku con backtracking
def resolver_sudoku(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:  # Encontrar una casilla vacía
                for num in range(1, 10):  # Probar con números del 1 al 9
                    if es_valido(tablero, num, fila, col):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):  # Llamada recursiva
                            return True
                        tablero[fila][col] = 0  # Restablecer si no funciona
                return False
    return True

# Generar un tablero de sudoku completo
def generar_sudoku():
    tablero = crear_tablero()
    for _ in range(11):  # Se ponen 11 números al azar como "semilla"
        fila, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not es_valido(tablero, num, fila, col) or tablero[fila][col] != 0:
            fila, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        tablero[fila][col] = num
    resolver_sudoku(tablero)  # Resolver el tablero para obtener una solución completa
    return tablero

# Vaciar algunas celdas para crear un puzzle jugable
def generar_puzzle(tablero, vacios=40):
    puzzle = [fila[:] for fila in tablero]  # Copiar el tablero
    vaciar = 0
    while vaciar < vacios:
        fila, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[fila][col] != 0:
            puzzle[fila][col] = 0
            vaciar += 1
    return puzzle

# Mostrar puzzle y su resolución
def mostrar_puzzle_y_solucion():
    tablero = generar_sudoku()          # Genera un tablero completo resuelto
    puzzle = generar_puzzle(tablero)    # Genera el puzzle a partir del tablero resuelto

    print("Puzzle de Sudoku generado:")
    imprimir_tablero(puzzle)            # Muestra el puzzle inicial

    print("\nResolución del Sudoku:")
    resolver_sudoku(puzzle)             # Resuelve el puzzle generado
    imprimir_tablero(puzzle)            # Muestra la solución

# Ejecuta la función para mostrar el puzzle y la solución
mostrar_puzzle_y_solucion()
