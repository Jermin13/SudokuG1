from flask import Flask, render_template, jsonify, session
import sudoku  # Asegúrate de que el archivo sudoku.py esté en el mismo directorio
import os
import time  # Importa el módulo time para medir el tiempo

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    if 'puzzle_inicial' not in session:
        inicio_generacion = time.time()  # Marca el tiempo de inicio de generación
        tablero_completo = sudoku.generar_sudoku()
        puzzle = sudoku.generar_puzzle(tablero_completo)
        fin_generacion = time.time()  # Marca el tiempo de fin de generación
        # Guarda el tiempo de generación en la sesión
        session['tiempo_generacion'] = fin_generacion - inicio_generacion
        session['puzzle_inicial'] = puzzle
    else:
        puzzle = session['puzzle_inicial']
    return render_template("index.html", puzzle=puzzle)

@app.route("/resolver", methods=["POST"])
def resolver():
    puzzle = session.get('puzzle_inicial')
    tiempo_generacion = session.get('tiempo_generacion', 0)  # Obtiene el tiempo de generación
    if puzzle:
        puzzle_a_resolver = [fila[:] for fila in puzzle]
        inicio_resolucion = time.time()  # Marca el tiempo de inicio de resolución
        tiempo_resolucion = sudoku.resolver_sudoku(puzzle_a_resolver)
        fin_resolucion = time.time()  # Marca el tiempo de fin de resolución

        tiempo_total = (fin_resolucion - inicio_resolucion) + tiempo_generacion  # Suma tiempos
        return jsonify({
            "solucion": puzzle_a_resolver,
            "tiempo_resolucion": round(tiempo_total, 6)  # Redondea el tiempo total a 6 decimales
        })
    else:
        return jsonify({"error": "No hay un puzzle para resolver"}), 400

@app.route("/nuevo")
def nuevo_puzzle():
    session.pop('puzzle_inicial', None)
    session.pop('tiempo_generacion', None)  # Limpia el tiempo de generación
    return home()

if __name__ == "__main__":
    app.run(debug=True)
