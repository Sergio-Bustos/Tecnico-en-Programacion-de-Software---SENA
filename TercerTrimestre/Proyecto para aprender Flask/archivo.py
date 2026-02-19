# Importamos Flask y la función render_template
# Flask: para crear la aplicación web
# render_template: para renderizar archivos HTML desde la carpeta 'templates'
from flask import Flask, render_template

# Creamos una instancia de la aplicación Flask
# __name__ se usa para indicar el punto de entrada principal de la aplicación
app = Flask(__name__)

# Definimos una ruta principal ("/") de la aplicación
# Cuando un usuario entre a la URL raíz (ej: http://127.0.0.1:5000/)
# se ejecutará la función 'index'
@app.route("/")
def index():
    # Esta función renderiza la plantilla 'index.html'
    # y le pasa una variable 'titulo' con el valor "Desarrollo Web con Flask y Jinja2"
    return render_template("index.html", titulo="Desarrollo Web con Flask y Jinja2")

# Punto de entrada del programa
# Si este archivo se ejecuta directamente (python app.py), Flask iniciará el servidor
if __name__ == "__main__":
    # Inicia la aplicación en modo debug
    # debug=True permite ver errores detallados y reinicia el servidor automáticamente al guardar cambios
    app.run(debug=True)  # debug=True solo en desarrollo



# En otras palabras este codigo;
# from flask import flask,render_template
# app = Flas(__name__)
#@app.route("/")
#def index():
# return render_template("index.html",titulo= "")
# if __name__ == "__main__":
# app.run(debug=True)