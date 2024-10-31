import random
import time

# Crear un tablero vacío de sudoku

def crear_tablero():
    
    return [[0 for _ in range(9)] for _ in range(9)]

# Imprimir el tablero 
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
    if num in tablero[fila]:
        return False
    if num in [tablero[i][col] for i in range(9)]:
        return False
    caja_fila, caja_col = (fila // 3) * 3, (col // 3) * 3
    for i in range(caja_fila, caja_fila + 3):
        for j in range(caja_col, caja_col + 3):
            if tablero[i][j] == num:
                return False
    return True

# Resolver el sudoku con backtracking y medir el tiempo de ejecución
def resolver_sudoku(tablero):
    inicio = time.time()  # Marca el tiempo de inicio
    def backtracking(tablero):
        for fila in range(9):
            for col in range(9):
                if tablero[fila][col] == 0:  # Encontrar una casilla vacía
                    for num in range(1, 10):
                        if es_valido(tablero, num, fila, col):
                            tablero[fila][col] = num
                            if backtracking(tablero):
                                return True
                            tablero[fila][col] = 0
                    return False
        return True

    backtracking(tablero)  # Llamada a la función de backtracking
    fin = time.time()      # Marca el tiempo de fin

    tiempo_resolucion = (fin - inicio)   # Tiempo total en segundos
    return round(tiempo_resolucion, 24)  # Devuelve el tiempo de resolución con 6 decimales

# Generar un tablero de sudoku completo
def generar_sudoku():
    tablero = crear_tablero()
    for _ in range(11):
        fila, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not es_valido(tablero, num, fila, col) or tablero[fila][col] != 0:
            fila, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        tablero[fila][col] = num
    resolver_sudoku(tablero)
    return tablero

# Vaciar algunas celdas para crear un puzzle jugable
def generar_puzzle(tablero, vacios=40):
    puzzle = [fila[:] for fila in tablero]
    vaciar = 0
    while vaciar < vacios:
        fila, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[fila][col] != 0:
            puzzle[fila][col] = 0
            vaciar += 1
    return puzzle
